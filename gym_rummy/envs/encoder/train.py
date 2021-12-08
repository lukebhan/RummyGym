import numpy as np
import torch
from autoencoder import AE
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

model = AE()

l = torch.nn.MSELoss()

optimizer = torch.optim.Adam(model.parameters(), 
        lr = 1e-4, 
        weight_decay = 1e-8)

data = np.loadtxt('deckdata.txt')
tensor = torch.from_numpy(data).float()

epochs = 5000
outputs = []
losses = []
batch_size = 19000
for epoch in range(epochs):
    permutation = torch.randperm(tensor.size()[0])
    running_loss = 0.0
    for i in range(0, tensor.size()[0], batch_size):
        optimizer.zero_grad()
        indexs = permutation[i:i+batch_size]
        data = tensor[indexs]
        output = model(data)

        loss = l(output, data)

        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    losses.append(running_loss)
    print(running_loss)
print("final score:", l(tensor,model(tensor))/tensor.size()[0])
torch.save(model.state_dict(), 'ae.pt')
plt.yscale('log')
plt.plot(losses)
plt.xlabel("Epoch Number")
plt.ylabel("Loss of Epoch")
plt.savefig("Loss.png")
plt.show()
