import torch
import torch.nn as nn
import torch.nn.functional as F
import os

__all__ = [
    "baseline",
    "baseline_seed1",
    "baseline_seed2",
    "baseline_seed3",
    "baseline_seed4",
    "baseline_seedn",
    "baseline_unfreeze",
    "baseline_unfreeze_seed1",
    "baseline_unfreeze_seed2",
    "baseline_unfreeze_seed3",
    "baseline_unfreeze_seed4",
    "baseline_unfreeze_seedn",
    "v1",
    "v2",
    "v3",
    "v4",
    "v5",
]

class cifar10_nn(nn.Module):
    def __init__(self,output_size):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, output_size)
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = x - torch.max(x)
        return F.log_softmax(x)


def _cifar10_nn(weights_name, pretrained, output_size=10):
    model = cifar10_nn(output_size=10)
    if pretrained:
        script_dir = os.path.dirname(__file__)
        state_dict = torch.load(
            script_dir + "/state_dicts/cifar10_nn_" + weights_name + ".pt",
        )
        model.load_state_dict(state_dict)
    return model

def _cifar10_model(weights_name, pretrained, output_size=10):
    model = cifar10_nn(output_size=10)
    if pretrained:
        script_dir = os.path.dirname(__file__)
        state_dict = torch.load(
            script_dir + "/state_dicts/cifar10_model_" + weights_name + ".pt",
        )
        model.load_state_dict(state_dict)
    return model


def baseline(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_seed1(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_seed1",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_seed2(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_seed2",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_seed3(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_seed3",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_seed4(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_seed4",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_seedn(pretrained=False, output_size=10, seed=0):
    return _cifar10_model(
        weights_name="baseline_seed_" + str(seed),
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_unfreeze(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_unfreeze",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_unfreeze_seed1(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_unfreeze_seed1",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_unfreeze_seed2(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_unfreeze_seed2",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_unfreeze_seed3(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_unfreeze_seed3",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_unfreeze_seed4(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="baseline_unfreeze_seed4",
        pretrained=pretrained,
        output_size=output_size
    )

def baseline_unfreeze_seedn(pretrained=False, output_size=10, seed=0):
    return _cifar10_model(
        weights_name="baseline_unfreeze_seed_" + str(seed),
        pretrained=pretrained,
        output_size=output_size
    )

def v1(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="pretrained_v1",
        pretrained=pretrained,
        output_size=output_size
    )

def v2(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="pretrained_v2",
        pretrained=pretrained,
        output_size=output_size
    )

def v3(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="pretrained_v3",
        pretrained=pretrained,
        output_size=output_size
    )

def v4(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="pretrained_v4",
        pretrained=pretrained,
        output_size=output_size
    )

def v5(pretrained=False, output_size=10):
    return _cifar10_nn(
        weights_name="pretrained_v5",
        pretrained=pretrained,
        output_size=output_size
    )

