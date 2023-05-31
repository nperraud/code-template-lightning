from torch import nn


class MLP(nn.Module):
    """Multi-layer perceptron model.

    It uses leaky ReLU as activation function and the last layer is a
    linear layer.

    Parameters
    ----------
    input_dim : int
        Dimension of the input.
    hidden_dim : int
        Dimension of the hidden layers.
    output_dim : int
        Dimension of the output.
    n_layers : int
        Number of hidden layers.
    use_softmax : bool
        Whether to use softmax as the activation function of the last layer.
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int,
        output_dim: int,
        n_layers: int = 3,
        use_softmax: bool = False,
    ):
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.n_layers = n_layers

        self.layers = nn.ModuleList()
        self.layers.append(nn.Linear(input_dim, hidden_dim))
        self.use_softmax = use_softmax
        for _ in range(n_layers - 1):
            self.layers.append(nn.Linear(hidden_dim, hidden_dim))
        self.layers.append(nn.Linear(hidden_dim, output_dim))

    def forward(self, x):
        x = x.view(-1, self.input_dim)
        for layer in self.layers[:-1]:
            x = layer(x)
            x = nn.functional.leaky_relu(x)
        x = self.layers[-1](x)
        if self.use_softmax:
            x = nn.functional.softmax(x, dim=1)
        return x
