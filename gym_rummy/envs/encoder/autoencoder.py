import numpy as np
import torch

class AE(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = torch.nn.Sequential(
                torch.nn.Linear(52, 36), 
                torch.nn.ReLU(),
                torch.nn.Linear(36, 16), 
                torch.nn.ReLU(),
                torch.nn.Linear(16, 8))

        self.decoder = torch.nn.Sequential(
                torch.nn.Linear(8, 16),
                torch.nn.ReLU(),
                torch.nn.Linear(16, 36), 
                torch.nn.ReLU(),
                torch.nn.Linear(36, 52), 
                torch.nn.ReLU())

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

    def encode(self, x):
        return self.encoder(x)
