import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision import transforms

from model.model import SampleModel
sys.path.append(os.path.abspath('..'))
import imagenet_class


img = cv2.imread('../baseball.png')
img = cv2.resize(img, (256, 256))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_tensor = transforms.ToTensor()(img)
img_tensor = img_tensor.unsqueeze_(0)

model = SampleModel()

output = model(img_tensor)
output = np.argmax(output.detach().numpy())

print(imagenet_class.target[str(output)][1])

plt.imshow(img)
plt.show()
