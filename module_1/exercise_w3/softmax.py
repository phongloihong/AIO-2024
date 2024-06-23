import torch
import torch.nn as nn
import math


class SoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def __call__(self, data: torch.Tensor) -> torch.Tensor:
        return self.forward(data)

    def forward(self, data: torch.Tensor) -> torch.Tensor:
        exp_x = torch.exp(data)
        sum_exp_x = sum(exp_x)
        result = torch.round(exp_x/sum_exp_x, decimals=4)

        return result


class SoftMaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def __call__(self, data: torch.Tensor) -> torch.Tensor:
        return self.forward(data)

    def forward(self, data) -> torch.Tensor:
        x_max = max(data)
        exp_x = torch.exp(data - x_max)
        sum_exp_x = sum(exp_x)
        result = torch.round(exp_x/sum_exp_x, decimals=4)

        return result


data = torch.Tensor([1, 2,  3])

soft_max = SoftMax()
assert torch.equal(soft_max(data), torch.Tensor([0.0900, 0.2447, 0.6652]))

soft_max_stable = SoftMaxStable()
assert torch.equal(soft_max_stable(data), torch.Tensor([0.09, 0.2447, 0.6652]))
