import torch
import torch.nn as nn
import math


class SoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def __call__(self, data: torch.Tensor) -> torch.Tensor:
        return self.forward(data)

    def forward(self, data: torch.Tensor) -> torch.Tensor:
        data_len = len(data)
        exp_x = [math.exp(i) for i in data]
        sum_exp_x = sum(exp_x)
        result = [round(exp_x[i]/sum_exp_x, 4) for i in range(data_len)]

        return torch.Tensor(result)


class SoftMaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def __call__(self, data: torch.Tensor) -> torch.Tensor:
        return self.forward(data)

    def forward(self, data) -> torch.Tensor:
        data_len = len(data)
        x_max = max(data)
        exp_x = [math.exp(i - x_max) for i in data]
        sum_exp_x = sum(exp_x)
        result = [round(exp_x[i]/sum_exp_x, 4) for i in range(data_len)]

        return torch.Tensor(result)


data = torch.Tensor([1, 2, 3])

soft_max = SoftMax()
assert torch.equal(soft_max(data), torch.Tensor([0.0900, 0.2447, 0.6652]))

soft_max_stable = SoftMaxStable()
assert torch.equal(soft_max_stable(data), torch.Tensor([0.09, 0.2447, 0.6652]))
