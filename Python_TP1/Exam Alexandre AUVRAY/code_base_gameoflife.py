import os
import time
import random

def clear_screen_windows():
    os.system("cls")

def clear_screen_unix():
    os.system("clear")

def random_boolean():
    return bool(random.getrandbits(1))

def to_string(game_of_life):
    s = "┌" + ("─" * (game_of_life.width * 2)) + "┐\n"
    for y in range(game_of_life.height):
        s += "│"
        for x in range(game_of_life.width):
            if game_of_life.grid[y][x]:
                s += "▓▓"
            else:
                s += "  "
        s += "│\n"
    s += "└" + ("─" * (game_of_life.width * 2)) + "┘\n"
    return s

class GameOfLife:
    def __init__(self, width=50, height=50, randomize = True):
        self.height = height
        self.width = width
        self.grid = list()
        for i in range(height):
            ligne = []
            for j in range(width):
                if randomize :
                    ligne.append(random_boolean())
                else :
                    ligne.append(False)
            self.grid.append(ligne)

    def set_cell(self, x, y):
        entre = input("True or False?")
        if entre.lower() == "true":
            self.grid[y][x] = True
        elif entre.lower() == "false":
            self.grid[y][x] = False
        else:
            print("Mauvais input")

    def is_alive(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.grid[y][x]

    def autour(self, x, y):
        vivants = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x + i < self.width and 0 <= y + j < self.height:
                    if self.grid[y + j][x + i]:
                        vivants += 1
        return vivants

    def update(self):
        new_grid = [[False for ab in range(self.width)] for ab in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                voisins_vivants = self.autour(x, y)
                if self.is_alive(x, y):
                    if voisins_vivants < 2 or voisins_vivants > 3:
                        new_grid[y][x] = False
                    else:
                        new_grid[y][x] = True
                else:
                    if voisins_vivants == 3:
                        new_grid[y][x] = True
        self.grid = new_grid
    def blinker(self, x, y, horiz = False):
        if horiz :
            assert 1 <= x < self.width - 1
            assert 0 <= y < self.height
            self.grid[y][x - 1] = True
            self.grid[y][x] = True
            self.grid[y][x + 1] = True
        else :
            assert 0 <= x < self.width
            assert 1 <= y < self.height - 1
            self.grid[y - 1][x] = True
            self.grid[y][x] = True
            self.grid[y + 1][x] = True

    def block(self, x, y):
        assert 0 <= x < self.width - 1
        assert 0 <= y < self.height - 1

        self.grid[y][x] = True
        self.grid[y][x + 1] = True
        self.grid[y + 1][x] = True
        self.grid[y + 1][x + 1] = True

    def glider(self, x, y):
        assert 0 <= x < self.width - 2
        assert 0 <= y < self.height - 2

        self.grid[y][x + 1] = True
        self.grid[y + 1][x + 2] = True
        self.grid[y + 2][x] = True
        self.grid[y + 2][x + 1] = True
        self.grid[y + 2][x + 2] = True

    def beacon(self, x, y):
        assert 0 <= x < self.width - 3
        assert 0 <= y < self.height - 3
        self.block(x, y)
        self.block(x + 2, y + 2)

    def pulsar(self, x, y):
        assert 0 <= x < self.width - 12
        assert 0 <= y < self.height - 12
        for i in [-6, -1, 1, 6]:
            self.blinker(x + i + 6, y, horiz=True)
            self.blinker(x, y + i + 6, horiz=False)

    def bee_hive(self, x, y):
        assert 0 <= x < self.width - 3
        assert 0 <= y < self.height - 2

        self.grid[y][x + 1] = True
        self.grid[y][x + 2] = True
        self.grid[y + 1][x] = True
        self.grid[y + 1][x + 3] = True
        self.grid[y + 2][x + 1] = True
        self.grid[y + 2][x + 2] = True

    def figures(self,name, x ,y):
        if name.lower() == "blinker" :
            self.blinker(x, y)
        if name.lower() == "block" :
            self.block(x, y)
        if name.lower() == "glider" :
            self.glider(x, y)
        if name.lower() == "beacon" :
            self.beacon(x, y)
        if name.lower() == "pulsar" :
            self.pulsar(x, y)
        if name.lower() == "bee_hive" :
            self.bee_hive(x, y)

test = GameOfLife()
block = input("Appuyez sur enter pour lancer le programme.")
while True:
    print(to_string(test))
    test.update()
    time.sleep(0.2)
    #test.figures(self,blinker,11, 11)
    clear_screen_unix()



