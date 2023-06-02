import torch

print(torch.version)
print(torch.version.cuda)
test = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(test)

