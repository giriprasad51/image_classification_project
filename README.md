# Fine-tuning Transformers For Image Classification

| name        | self - supervised                           | initialized checkpoint                                                                                    | crop size | #params | accuracy | Kaggle Notebook                                                                                               |
| :---------- | :------------------------------------------ | :-------------------------------------------------------------------------------------------------------- | :-------: | :-----: | :------- | :------------------------------------------------------------------------------------------------------------ |
| ViT | <span style="color:red">[ ✗ ]</span>        | [vit_checkpoint](https://www.kaggle.com/code/giriprasad512/cifar-10-vitforimageclassification/output)             |  224x224  | 85M  | 0.9561   | [cifar-10-mobilevit-s.ipynb](https://www.kaggle.com/code/giriprasad512/cifar-10-vitforimageclassification)
| BEiT        | <span style="color:lightgreen">[ ✓ ]</span> | [beit_checkpoint](https://www.kaggle.com/code/giriprasad512/cifar-10-by-fine-tuning-beit/output) |  224x224  |   87M   | 0.9505   | [cifar-10-by-fine-tuning-beit.ipynb](https://www.kaggle.com/code/giriprasad512/cifar-10-by-fine-tuning-beit/) | 
| mobilevit_s | <span style="color:red">[ ✗ ]</span>        | [model.pth](checkpoints/model.pth)             |  224x224  | 5M   | 0.8900   | [cifar-10-mobilevit-s.ipynb](https://www.kaggle.com/code/giriprasad512/cifar-10-mobilevit-s)                  |


## Setup

First, clone the repo and install required packages:

```
!git clone https://github.com/giriprasad51/image_classification_project.git
cd image_classification_project
pip install -r requirements.txt
```

## Demo

<!-- [![Watch the video](thumnail.png)](https://github.com/giriprasad51/image_classification_project/blob/main/video.mp4) -->

![GIF](gif1.gif)

## Confusion Matrixs
<!DOCTYPE html>
<html lang="en">
<body>

<div class="container">
  <div class="image-container">
    <figure>
        <img src="confusion_matrices\Vit_confusion_matrix.png" alt="Confusion Matrix 2" style="width: 300px; height: 200px;">
         <figcaption style="text-align:center;">  ViT </figcaption> 
    </figure>
  </div>
  <div class="image-container">
    <figure>
        <img src="confusion_matrices\BEiT_confusion_matrix.png" alt="Confusion Matrix 1" style="width: 300px; height: 200px;">
        <figcaption style="text-align:center;"> BEiT </figcaption>
    </figure> 
  </div>
  <div class="image-container">
    <figure>
        <img src="confusion_matrices\mobilevit_s_confusion_matrix.png" alt="Confusion Matrix 2" style="width: 300px; height: 200px;">
         <figcaption style="text-align:center;">  mobilevit_s </figcaption> 
    </figure>
  </div>
</div>

</body>
</html>

