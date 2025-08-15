Dataset **Annotated Quantitative Phase Microscopy Cell** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMjMzOF9Bbm5vdGF0ZWQgUXVhbnRpdGF0aXZlIFBoYXNlIE1pY3Jvc2NvcHkgQ2VsbC9hbm5vdGF0ZWQtcXVhbnRpdGF0aXZlLXBoYXNlLW1pY3Jvc2NvcHktY2VsbC1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJXbmt6bDE3bFcwcnZBMXdvVXFUWkdzaTBXNjJ1QndrSkhyTURjUk9ucHB3PSJ9?response-content-disposition=attachment%3B%20filename%3D%22annotated-quantitative-phase-microscopy-cell-DatasetNinja.tar%22)

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
