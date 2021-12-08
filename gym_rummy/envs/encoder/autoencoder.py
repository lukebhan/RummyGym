"""Creates the autoencoder"""

#import numpy as np
import torch

class AE(torch.nn.Module):
    """Autoencoder class"""

    def __init__(self):
        """Initializes the auto encoder by creating encoder and decoder functions"""
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

    def forward(self, num):
        """Encodes and decodes x"""
        encoded = self.encoder(num)
        decoded = self.decoder(encoded)
        return decoded

    def encode(self, x):
        return self.encoder(x)
