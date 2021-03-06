
import random
import sys

num_of_columns = 7
num_of_rows = 6

# rows count goes from bottom to top
# columns count goes from left to right

class gameboard():
    def __init__(self):
        self.columns = []
        for i in range(0, num_of_columns):
            self.columns.append([])
        
    # check whether column i is full
    def column_full(self, i):
        return len(self.columns[i])==num_of_rows

    # drop a disc on column i
    def drop_disc(self, i, d):
        if not self.column_full(i):
            self.columns[i].append(d)

    # convert column i to a string
    def column2string(self, i):
        assert i>=0 and i<num_of_columns
        return ''.join(self.columns[i])

    # convert row i to a string
    def row2string(self, i):
        assert i>=0 and i<num_of_rows
        t = []
        for col in self.columns:
            try:
                t.append(col[i])
            except:
                t.append(' ')
        return ''.join(t)

    # check whether there is a hit on a col
    def check_vertical(self, i):
        s = self.column2string(i)
        if 'oooo' in s or 'xxxx' in s:
            print "column {0} bingo!".format(i)
            return True
        else:
            return False
 
    # check whether there is a hit on a row
    def check_horizontal(self, i):
        s = self.row2string(i)
        if 'oooo' in s or 'xxxx' in s:
            print "row {0} bingo!".format(i)
            return True
        else:
            return False
    
    # return ele of row x, col y
    def get_xy(self, x, y):
        assert x>=0 and x<num_of_columns
        assert y>=0 and y<num_of_rows
        e = None
        try:
            e = self.columns[x][y]
        except:
            e = None
        
    def diag2string(self, x, y):
        chars = []
        i, j = x,y
        done = False
        try:
            while not done:
                c = self.get_xy(i,j)
                if c:
                    chars.append(c)
                    i += 1
                    j += 1
                else:
                    done = True
        except:
            pass
        s = ''.join(chars)
        return s

    # check where there is a hit on diagonal
    def check_diagnonal(self):
        for c in range(0, num_of_columns):
            s = self.diag2string(c, 0)
            if 'oooo' in s or 'xxxx' in s:
                print "diag {0},{1} bingo!".format(c, 0)
                return True
        for r in range(0, num_of_rows):
            s = self.diag2string(0, r)
            if 'oooo' in s or 'xxxx' in s:
                print "diag {0},{1} bingo!".format(0, r)
                return True
        return False

    def print_col(self, i):
        assert i>=0 and i<= num_of_columns
        s = self.column2string(i)
        print s

    def print_row(self, i):
        assert i>=0 and i<= num_of_rows
        s = self.row2string(i)
        print s

    def print_gameboard(self):
        print "----------------------"
        l = list(reversed(range(num_of_rows)))
        for r in l:
            self.print_row(r)

    # check if there is a hit
    def check_four(self):
        for i in range(0, num_of_columns):
            if self.check_vertical(i):
                return True

        for i in range(0, num_of_rows):
            if self.check_horizontal(i):
                return True

        if self.check_diagnonal():
            return True

        return False

def randomdraw():
    return random.choice(['o','x'])

if __name__ == "__main__":
    
    gb = gameboard()
    for _ in range(0, num_of_rows):
        for c in range(0, num_of_columns):
            disc = randomdraw()
            #print "dropping disc {0} on column {1}".format(disc, c)
            gb.drop_disc(c, disc)
            gb.print_gameboard()
            if gb.check_four():
                print "we have a hit!!"
                sys.exit(0)

    """
    gb.print_gameboard()
    for c in range(0, num_of_columns):
        print "printing col {0} (rotated)".format(c)
        gb.print_col(c)

    for r in range(0, num_of_rows):
        print "printing row {0}".format(r)
        gb.print_row(r)
    """