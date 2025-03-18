import torch
import torch.nn as nn
import torch.optim as optim

# build the data

examples = torch.tensor(
    [[22, 25], [25, 35], [47, 80], [52, 95], [46, 82], [56, 90], [23, 27], [30, 50], [40, 60], [39, 57], [53, 95], [48, 88]],
    dtype=torch.float32
)

labels = torch.tensor(
    [[0], [0], [1], [1], [1], [1], [0], [1], [1], [0], [1], [1]],
    dtype=torch.float32
)

# build the model

model = nn.Sequential(
    nn.Linear(examples.shape[1], 1),
    nn.Sigmoid()
)

optimizer = optim.SGD(model.parameters(), lr=0.005)

criterion = nn.BCELoss() # binary cross-entropy loss

# train the model

print("Beginning training ...")

for step in range(1, 6001):
    optimizer.zero_grad()
    loss = criterion(model(examples), labels)
    loss.backward()
    optimizer.step()
    if step == 1 or step % 1000 == 0:
        print(f"Step {step}, Loss: {loss.item()}")

print("Done ✅")