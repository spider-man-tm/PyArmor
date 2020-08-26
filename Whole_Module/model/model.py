from torch import nn
from torchvision import models


class SampleModel(nn.Module):
    def __init__(self):
        super(SampleModel, self).__init__()
        self.backborn = models.vgg16(pretrained=True)

    def forward(self, x):
        x = self.backborn(x)
        return x
