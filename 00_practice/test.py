# Self-Attention
import torch
import torch.nn as nn

class selfAttention(nn.Module):
    def __init__(self, hidden_dim):
        super(selfAttention, self).__init__()
        # q,k,v matrix
        self.q = nn.Linear(hidden_dim, hidden_dim)
        self.k = nn.Linear(hidden_dim, hidden_dim)
        self.v = nn.Linear(hidden_dim, hidden_dim)
        self.scale = torch.sqrt(torch.FloatTensor([hidden_dim]))

    def forward(self, x):
        # x: (batch_size, seq_length, hidden_dim)
        query = self.q(x)
        key = self.k(x)
        value = self.v(x)
        score = torch.matmul(query, key.transpose(1,2)) / self.scale
        weight = torch.softmax(score, dim=-1)
        output = torch.matmul(weight, value)
        return output, weight

model = selfAttention(128)
x = torch.ones((10, 20, 128))
out = model(x)
print(model)