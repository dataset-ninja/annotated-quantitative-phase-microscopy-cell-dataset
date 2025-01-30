Dataset **Annotated Quantitative Phase Microscopy Cell** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzIzMzhfQW5ub3RhdGVkIFF1YW50aXRhdGl2ZSBQaGFzZSBNaWNyb3Njb3B5IENlbGwvYW5ub3RhdGVkLXF1YW50aXRhdGl2ZS1waGFzZS1taWNyb3Njb3B5LWNlbGwtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiTXFpYUpmcEsvcWVNQlpNSnBhb09WWWovOHpaSlRwWnppdzIxZHRxTHREUT0ifQ==)

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
