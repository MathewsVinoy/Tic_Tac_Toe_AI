import random
from agent import Agent

class TicTacToeAI:
    def __init__(self):
        self.a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.win=[(0,1,2),(1,3,6),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    def reset(self):
        self.a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']


    def printTable(self):
        print(f"| {self.a[0]} | {self.a[1]} | {self.a[2]} |")
        print(f"| {self.a[3]} | {self.a[4]} | {self.a[5]} |")
        print(f"| {self.a[6]} | {self.a[7]} | {self.a[8]} |")

    def addValues(self,n,value):
        if self.a[n-1]==' ':
            self.a[n-1]=value
        else:
            if value == 'x':
                n=int(input("that no is used plz re-enter : "))
                self.addValues(n,value)
            else:
                n=agent.get_action(self.a)
                self.addValues(n,value)
        self.printTable()


    def checkFunction(self):
        reward=0
        for tup in self.win:
            if  self.a[tup[0]]==self.a[tup[1]]==self.a[tup[2]]=='x':
                    # return "x wins"
                    reward=-10
                    game_over = True
                    print("ai lost")
                    return reward, game_over
            if self.a[tup[0]]==self.a[tup[1]]==self.a[tup[2]]=='o':
                    # return "o wins"
                    reward=10
                    game_over = True
                    print(" ai wins ")
                    return reward, game_over
        # return 0
        return reward, False

    def play_step(self,final_move):
        self.addValues(final_move,'o')
        reward, game_over=self.checkFunction()
        return reward, game_over
        

#     if flag==0:
#         print(draw)

