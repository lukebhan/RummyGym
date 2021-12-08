"""Trains the autoencoder for compressed state space"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import torch
from autoencoder import AE
matplotlib.use('qt5agg')

model = AE()

l = torch.nn.MSELoss()

optimizer = torch.optim.Adam(model.parameters(),
        lr = 1e-4,
        weight_decay = 1e-8)

data = np.loadtxt('deckdata.txt')
tensor = torch.from_numpy(data).float() #pylint: disable=E1101

EPOCHS = 5000
outputs = []
losses = []
BATCH_SIZE = 19000
for epoch in range(EPOCHS):
    permutation = torch.randperm(tensor.size()[0]) #pylint: disable=E1101
    RUNNING_LOSS = 0.0
    for i in range(0, tensor.size()[0], BATCH_SIZE):
        optimizer.zero_grad()
        indexs = permutation[i:i+BATCH_SIZE]
        data = tensor[indexs]
        output = model(data)

        loss = l(output, data)

        loss.backward()
        optimizer.step()

        RUNNING_LOSS += loss.item()
    losses.append(RUNNING_LOSS)
    print(RUNNING_LOSS)
print("final score:", l(tensor,model(tensor))/tensor.size()[0])
torch.save(model.state_dict(), 'ae.pt')
plt.yscale('log')
plt.plot(losses)
plt.xlabel("Epoch Number")
plt.ylabel("Loss of Epoch")
plt.savefig("Loss.png")
plt.show()
