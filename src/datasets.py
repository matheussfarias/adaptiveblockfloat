import torch
from torchvision import datasets, transforms


batch_cifar10 = 50
batch_mnist = 128
# CIFAR 10 dataset
transform_train = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

testset = datasets.CIFAR10(
    root='./datasets/CIFAR10', train=False, download=True, transform=transform_test)
testloader = torch.utils.data.DataLoader(
    testset, batch_size=batch_cifar10, shuffle=False)


# MNIST dataset
test_loader = torch.utils.data.DataLoader(
        datasets.MNIST('./datasets', train=False, download=True, transform=transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
            ])),
        batch_size=batch_mnist, shuffle=True)

