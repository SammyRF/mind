#fix1
import random
class Mind:
    def __init__(self, lbds, size = 19):
        self.lbds = lbds
        self.size = size
        self.pix = ('  ', ' *')
        self.mind = [[self.pix[random.randint(0, 1)] for _ in range(size)] for _ in range(size)]

    def next(self):
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        self.mind[x][y] = self.pix[self.fine(x, y)]

    def show(self):
        print("")
        for row in self.mind:
            print(''.join(row))

    def fine(self, x, y):
        return int(any([lbd(x - self.size // 2, y - self.size // 2) for lbd in self.lbds]))

    def finish(self):
        return sum(self.pix.index(self.mind[i][j]) == self.fine(i, j) \
            for i in range(self.size) \
            for j in range(self.size)) \
            == self.size ** 2

    def run(self):
        times = 0
        while not self.finish():
            self.next()
            times += 1
            if times % 500 == 0:
                self.show()
        self.show()
        print(times)

if __name__ == '__main__':
    ldbs = []
    ldbs.append(lambda x, y :  abs(x ** 2 + y ** 2 - 81) < 5)
    ldbs.append(lambda x, y :  x == 0 or y == 0)
    ldbs.append(lambda x, y :  x == y or x == - y)
    m = Mind(ldbs)
    m.run()

