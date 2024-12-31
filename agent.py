import torch 
import random
from helper import plot
from game import TicTacToeAI
from collections import deque
from model import QTrainer, Linear_QNet

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
        return array

    def remember(self,state_old, final_move, reward, state_new,done):
        self.memory.append((state,action,reward,next_state,done))
    
    def train_long_memory(self):
        if len(self.memory)>BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample=self.memory

        states,actions,rewards,next_states,dones=zip(*mini_sample)
        self.trainer.train_step(states,actions,rewards,next_states,dones)
    
    def train_short_memory(self,state_old, final_move, reward, state_new,done):
        self.trainer.train_step(state,action,reward,next_state,done)

    def get_action(self,state):
        self.epsilon = 80-self.n_games
        final_move = [0,0,0,0,0,0,0,0,0]
        if random.randint(0,200) <self.epsilon:
            move = random.randint(1,9)
            final_move[move-1]=1
        else:
            state0=torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move-1]=1
        return final_move
        

def train():
    plot_scores = []
    plot_mean_scores=[]
    total_score =0
    record =0
    agent = Agent()
    game = TicTacToeAI()
    while True:
        a=int(input("Enter the no b/w 1-9 : "))
        game.addValues(a,'x')
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done = game.play_step(final_move)
        state_new = agent.get_state(game)
        agent.train_short_memory(state_old, final_move, reward, state_new,done)
        agent.remember(state_old,final_move,reward,state_new,done)
        if done:
            game.reset()
            agent.n_games +=1
            agent.train_long_memory()
            agent.model.save()
            plot_scores.append(score)
            total_score +=score
            mean_scores = total_score/agent.n_games
            plot_mean_scores.append(mean_scores)
            plot(plot_scores, plot_mean_scores)

if __name__ =="__main__":
    train()