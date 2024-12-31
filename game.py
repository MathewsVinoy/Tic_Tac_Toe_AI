import random

class TicTacToeAI:
    def __init__(self):
        self.a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.win=[(0,1,2),(1,3,6),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

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
                n=random.randint(1,9)
                self.addValues(n,value)


    def checkFunction(self):
        for tup in self.win:
            if  self.a[tup[0]]==self.a[tup[1]]==self.a[tup[2]]=='x':
                    return "x wins"
            if self.a[tup[0]]==self.a[tup[1]]==self.a[tup[2]]=='o':
                    return "o wins"
        return 0

# def gameLoop():
#     game = TicTacToeAI()
#     game.printTable()
#     flag=0
#     for i in range(9):
#         if(i%2==0):
#             a=int(input("Enter the no b/w 1-9 : "))
#             game.addValues(a,'x')
#         else:
#             a=random.randint(1,9)
#             a=game.addValues(a,'o')
#         game.printTable()
#         flag=game.checkFunction()
#         if flag!=0:
#             print(flag)
#             break

#     if flag==0:
#         print(draw)

