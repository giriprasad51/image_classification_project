
import timm
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms 
# from torchvision.utils import make_grid
from PIL import Image
import os
import random
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from torch.optim.lr_scheduler import StepLR
from tqdm import tqdm
%matplotlib inline

import warnings
warnings.filterwarnings("ignore")

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
print(class_names)
print(len(class_names))
N=list(range(len(class_names)))
normal_mapping=dict(zip(class_names,N)) 
reverse_mapping=dict(zip(N,class_names))
print(normal_mapping,reverse_mapping)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

class MyModel(nn.Module):

    def __init__(self, model_name='mobilevit_s', pretrained=True):
        super(MyModel, self).__init__()
        self.model = timm.create_model(model_name, pretrained, in_chans=3)
        self.fc1 = nn.Linear(1000,16)
        self.fc2 = nn.Linear(16,64)        
        self.fc3 = nn.Linear(64,len(class_names))
        
    def forward(self, x):
        #print(x.shape)
        x = self.model(x)
        #print(x.shape)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        #print(x.shape)
        return x
    
# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Move model to GPU
model = MyModel()
model.load_state_dict(torch.load('./model.pth', map_location=torch.device('cpu')))
model.to(device)

def classify_image(image):
    img = image.convert('RGB')       
    img = transform(img).unsqueeze(0)
    pred = model(img).argmax(dim=1)
    return reverse_mapping[pred.item()]