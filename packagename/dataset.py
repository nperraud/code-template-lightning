from torchvision.datasets import MNIST
from packagename.conf import DATASETDIR
from torchvision import datasets, transforms
from torch.utils.data import TensorDataset, DataLoader, random_split

def load_mnist():
    """ Load the MNIST dataset."""

    # transforms for images
    transform=transforms.Compose([transforms.ToTensor(), 
                                transforms.Normalize((0.1307,), (0.3081,))])
    mnist_train = MNIST(DATASETDIR, train=True, download=True, transform=transform)
    assert len(mnist_train) == 60000
    mnist_train, mnist_val = random_split(mnist_train, [55000, 5000])

    mnist_test = MNIST(DATASETDIR, train=False, download=True, transform=transform)
    assert len(mnist_test) == 10000
    return mnist_train, mnist_val, mnist_test