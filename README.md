# Catch Basin Classifier
A catch basin classifier written in Python, Tensorflow, and Keras.

## Setting Up

**NOTE**: *A saved model's file name is in format: `model-{number}-{training accuracy}-{validation accuracy}-{training loss}-{validation loss}`*

1. Clone the repo: `$ git clone github.com/SnkSynthesis/catch_basin_classifier`.
2. Open project in Jupyter Lab or Jupyter Notebook:
   * Run all cells of `object_localizer_model.ipynb`
   * Run all cells of `image_classifier_model.ipynb`
3. Update two lines of `config.py` (example file name: `model-0-0.65-0.54-0.7-1.09`):
```python
# Following values must be changed if there are no saved models or a different model needs to be used.
image_classifier_model_name = 'FILE NAME OF DESIRED MODEL IN saved_models/image_classifier_models'
object_localizer_model_name = 'FILE NAME OF DESIRED MODEL IN saved_models/object_classifier_models'
```
4. Run `$ python pipeline.py`. Running `pipeline.py` will:
   * Loads models based on `config.py`.
   * Prompts for path of image to predict upon
   * Shows the image with bounding box prediction of object_localizer_model (given image with red bounding box)
   * Shows prediction of image_classifier_model (in both one-hot-encoded and text format)

## Workflow
<img src="workflow.png" width="40%" height="40%"></img>
