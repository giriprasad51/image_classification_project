
import torch
import timm
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
img = Image.open(path).convert('RGB')
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

if transform is not None:
    img = transform(img)

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
    
model = MyModel() 

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.eval()
pred = model(img).argmax(dim=1)
print(pred)