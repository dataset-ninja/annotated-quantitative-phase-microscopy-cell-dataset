Dataset **Annotated Quantitative Phase Microscopy Cell** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/c/7/9l/Gfz0da5PYmcUI5QcPfPW9QG9EZfuIbtCtd8MXjkaaB44lY3AgBvyeC3l95rnjjay8ftiU3zBShGC9SUgfrD1tCow0iel5FQ8BAJiO864aqw0ZM5F55vGcUDoFo7Q.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Annotated Quantitative Phase Microscopy Cell', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [labelled.zip](https://zenodo.org/record/5153251/files/labelled.zip?download=1)
- [unlabelled.zip](https://zenodo.org/record/5153251/files/unlabelled.zip?download=1)
