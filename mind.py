import random
class Mind:
    def __init__(self, lbd, size = 19):
        self.lbd = lbd
        self.size = size
        self.pix = ('  ', ' *')
        self.mind = [[self.pix[random.randint(0, 1)] for _ in range(size)] for _ in range(size)]

    def next(self):
        x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        self.mind[x][y] = self.pix[self.lbd(x, y)]

    def show(self):
        print("")
        for row in self.mind:
            print(''.join(row))

    def finish(self):
        return sum(self.pix.index(self.mind[i][j]) == self.lbd(i, j) \
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
    m = Mind(lambda x, y : x == 19 - y)
    m.run()

