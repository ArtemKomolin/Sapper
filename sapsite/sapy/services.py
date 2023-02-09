from tkinter import *
from tkinter import messagebox
from .views import *
import random

class Cell:
    def __init__(self, around_mines = 0, mine = False, num=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
        self.num = num

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell(0, False, i + 10*j) for i in range(1, self.N+1)] for j in range(self.N)]
        self.init()

    def init(self):
        m = 0
        while m < self.M:
            r = random.randint(0, self.N - 1)
            c = random.randint(0, self.N - 1)
            if self.pole[r][c].mine:
                continue
            self.pole[r][c].mine = True
            m += 1

        # счетчик кол-ва мин вокруг клетки
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

        for r in range(self.N):
            for c in range(self.N):
                if not self.pole[r][c].mine:
                    mines = sum((self.pole[r+i][c+j].mine for i, j in indx if 0 <= r+i < self.N and 0 <= c+j < self.N))
                    self.pole[r][c].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))

    def show2(self):
        return self.pole

    def show3(self):
        for r in range(self.N):
            for c in range(self.N):
                print(self.pole[r][c].__dict__)



pole_game = GamePole(10, 12)
c1 = Cell()


