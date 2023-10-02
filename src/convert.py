# https://zenodo.org/record/5153251#.YlAixn9Bzmg

import os

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from PIL import Image
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_name,
    get_file_name_with_ext,
)


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count
    
def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:

    # project_name = "Quantitative phase microscopy cell"
    labelled_path = "/home/grokhi/rawdata/annotated-quantitative-phase-microscopy-cell-dataset/labelled"
    unlabelled_path = "/home/grokhi/rawdata/annotated-quantitative-phase-microscopy-cell-dataset/unlabelled"
    batch_size = 3

    ds_name_to_data = {"labelled": labelled_path, "unlabelled": unlabelled_path}


    image_suffix = "_img.tif"
    mask_suffix = "_mask.png"


    def create_ann(image_path):
        labels = []

        obj_class = meta.get_obj_class(image_path.split("/")[-2])

        mask_path = image_path.split(image_suffix)[0] + mask_suffix

        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            img_height = mask_np.shape[0]
            img_wight = mask_np.shape[1]
            unique_pixels = np.unique(mask_np)[1:]
            for idx in unique_pixels:
                mask = mask_np == idx
                ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                for i in range(1, ret):
                    obj_mask = curr_mask == i
                    curr_bitmap = sly.Bitmap(obj_mask)
                    if curr_bitmap.area > 100:
                        curr_label = sly.Label(curr_bitmap, obj_class)
                        labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


    a2058 = sly.ObjClass("A2058", sly.Bitmap)
    g361 = sly.ObjClass("G361", sly.Bitmap)
    hob = sly.ObjClass("HOB", sly.Bitmap)
    pc3 = sly.ObjClass("PC3", sly.Bitmap)
    pnt1a = sly.ObjClass("PNT1A", sly.Bitmap)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[a2058, g361, hob, pc3, pnt1a])
    api.project.update_meta(project.id, meta.to_json())


    for ds_name, data_path in ds_name_to_data.items():
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        if ds_name == "labelled":
            all_data = os.listdir(data_path)

            for curr_data in all_data:
                curr_path = os.path.join(data_path, curr_data)
                all_items = os.listdir(curr_path)
                images_names = [
                    item_name for item_name in all_items if item_name.endswith(image_suffix)
                ]

                progress = sly.Progress("Create dataset {}".format(curr_data), len(images_names))

                for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                    img_pathes_batch = [os.path.join(curr_path, im_name) for im_name in img_names_batch]
                    # img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
                    img_nps_batch = [
                        np.array(Image.open(img_path).convert("RGB")) * 25
                        for img_path in img_pathes_batch
                    ]
                    img_infos = api.image.upload_nps(dataset.id, img_names_batch, img_nps_batch)
                    img_ids = [im_info.id for im_info in img_infos]

                    anns = [create_ann(image_path) for image_path in img_pathes_batch]
                    api.annotation.upload_anns(img_ids, anns)

                    progress.iters_done_report(len(img_names_batch))

        else:
            images_names = os.listdir(data_path)

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                img_pathes_batch = [os.path.join(data_path, im_name) for im_name in img_names_batch]
                # img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
                img_nps_batch = [
                    np.array(Image.open(img_path).convert("RGB")) * 25 for img_path in img_pathes_batch
                ]
                img_infos = api.image.upload_nps(dataset.id, img_names_batch, img_nps_batch)
                img_ids = [im_info.id for im_info in img_infos]

                progress.iters_done_report(len(img_names_batch))
    return project


