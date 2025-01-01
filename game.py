

class TicTacToeAI:
    def __init__(self):
        self.a = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        self.error = False
        self.moves = 0

    def reset(self):
        self.a = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.error = False
        self.moves = 0

    def printTable(self):
        print(f"| {self.a[0]} | {self.a[1]} | {self.a[2]} |")
        print(f"| {self.a[3]} | {self.a[4]} | {self.a[5]} |")
        print(f"| {self.a[6]} | {self.a[7]} | {self.a[8]} |\n")


    def addValues(self, n, value):
        if self.a[n] == ' ':
            self.moves += 1
            self.a[n] = value
            self.error = False
            self.printTable()
        else:
            if value == 'x':
                n = int(input("That no is used plz re-enter: "))
                self.addValues(n-1, value)
            else:
                self.error = True

    def checkFunction(self):
        reward = 0
        for tup in self.win:
            if self.a[tup[0]] == self.a[tup[1]] == self.a[tup[2]] == 'x':
                reward = -10
                game_over = True
                print("AI lost")
                return -10, True
            elif self.a[tup[0]] == self.a[tup[1]] == self.a[tup[2]] == 'o':
                print("AI wins")
                return 10, True
        if self.moves == 9:
            print("It's a tie")
            return 5, True

        return reward, False

    def play_step(self, final_move):
        n = final_move.index(1)
        self.addValues(n, 'o')
        reward, game_over = self.checkFunction()
        return reward, game_over
