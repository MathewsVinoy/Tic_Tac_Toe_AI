import torch 
from collections import deque
from game import TicTacToeAI

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR= 0.001

class Agent:
    def __init__(self):
        self.n_games =0
        self.epsilon =0
        self.gamma =0.9
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model= None
        self.trainer = None
    
    def get_state(self,game):
        array = game.a
        mapping = {'x':1,'o':2}
        array = [mapping.get(value,0) for value in array]

        return torch.tensor(array, dtype=torch.float)
    
    def remember():
        pass
    
    def train_full_memory(self):
        pass
    
    def train_short_memory(self):
        pass

    def get_action(self):
        pass

def train():
    pass

if __name__ =="__main__":
    train()