
import random

num_of_columns = 7
num_of_rows = 6

class gameboard():
    def __init__(self):
        self.columns = []

    # check whether column i is full
    def column_full(self, i):
        return len(self.columns[i])==num_of_rows

    # drop a disc on column i
    def drop_disc(self, i, d):
        if not column_full(self, i, d):
            self.columns[i].append(d)

    # check whether there is a hit on column i
    def check_vertical(self, i):
        return False

    # check whether there is a hit on row i
    def check_horizonta(self, i):
        return False
        
    # check where there is a hit on diagonal
    def check_diagnonal(self):
        return False

    def print_gameboard(self):
        pass

    # check if there is a hit
    def check_four(self):
        for i in range(0, num_of_columns):
            if check_vertical(self, i):
                return True

        for i in range(0, num_of_rows):
            if check_horizontal(self, i):
                return True

        if check_diagonal(self):
            return True

        return False

def randomdraw():
    return random.choice(['o','x'])

if __name__ == "__main__":
    gb = gameboard()

    done = False
    while not done:
        disc = randomdraw()
        print disc
