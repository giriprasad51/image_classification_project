<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Transformer-based Image Classification Comparison</title>
  <style>
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }
    .image-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-right: 20px;
    }
    .image-container img {
      width: 300px; /* Adjust this value as needed */
      height: auto;
    }
    .title {
      margin-top: 10px;
      text-align: center;
    }
    .table-container {
      margin-top: 50px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    th {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>

<div class="container">
  <div class="image-container">
    <img src="confusion_matrices\Vit_confusion_matrix.png" alt="Confusion Matrix for ViT">
    <p class="title">ViT</p>
  </div>
  <div class="image-container">
    <img src="confusion_matrices\BEiT_confusion_matrix.png" alt="Confusion Matrix for BEiT">
    <p class="title">BEiT</p>
  </div>
  <div class="image-container">
    <img src="confusion_matrices\mobilevit_s_confusion_matrix.png" alt="Confusion Matrix for mobilevit_s">
    <p class="title">mobilevit_s</p>
  </div>
</div>

<div class="table-container">
  <h2>Model Comparison</h2>
  <table>
    <tr>
      <th>Name</th>
      <th>Self-supervised</th>
      <th>Initialized Checkpoint</th>
      <th>Crop Size</th>
      <th>#Params</th>
      <th>Accuracy</th>
      <th>Kaggle Notebook</th>
    </tr>
    <tr>
      <td>ViT</td>
      <td>[ ✗ ]</td>
      <td><a href="https://www.kaggle.com/code/giriprasad512/cifar-10-vitforimageclassification/output">vit_checkpoint</a></td>
      <td>224x224</td>
      <td>85M</td>
      <td>0.9561</td>
      <td><a href="https://www.kaggle.com/code/giriprasad512/cifar-10-vitforimageclassification">cifar-10-mobilevit-s.ipynb</a></td>
    </tr>
    <tr>
      <td>BEiT</td>
      <td>[ ✓ ]</td>
      <td><a href="https://www.kaggle.com/code/giriprasad512/cifar-10-by-fine-tuning-beit/output">beit_checkpoint</a></td>
      <td>224x224</td>
      <td>87M</td>
      <td>0.9505</td>
      <td><a href="https://www.kaggle.com/code/giriprasad512/cifar-10-by-fine-tuning-beit/">cifar-10-by-fine-tuning-beit.ipynb</a></td>
    </tr>
    <tr>
      <td>mobilevit_s</td>
      <td>[ ✗ ]</td>
      <td><a href="checkpoints/model.pth">model.pth</a></td>
      <td>224x224</td>
      <td>5M</td>
      <td>0.8900</td>
      <td><a href="https://www.kaggle.com/code/giriprasad512/cifar-10-mobilevit-s">cifar-10-mobilevit-s.ipynb</a></td>
    </tr>
  </table>
</div>

<div>
  <h2>Setup</h2>
  <p>First, clone the repo and install required packages:</p>
  <pre><code>!git clone https://github.com/giriprasad51/image_classification_project.git
cd image_classification_project
pip install -r requirements.txt</code></pre>
</div>

<div>
  <h2>Demo</h2>
  <!-- <img src="thumnail.png" alt="Video Thumbnail" onclick="window.open('https://github.com/giriprasad51/image_classification_project/blob/main/video.mp4', '_blank')"> -->
  <img src="gif1.gif" alt="Demo GIF">
</div>

</body>
</html>
