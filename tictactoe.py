X = 'X'
O = 'O'


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.step = 0

    def mark(self, x, y):
        x, y = int(x) - 1, int(y) - 1

        if x > 2 or y > 2 or x < 0 or y < 0:
            print('Неправильные координаты')

        elif self.winner() in (O, X) or not self.free_spaces():
            print('Игра окончена')

        elif self.board[x][y] in (O, X):
            print('Недоступная клетка')

        elif self.step:
            self.board[x][y] = O
            self.step -= 1

        elif not self.step:
            self.board[x][y] = X
            self.step += 1

    def show(self):
        row = ['|'.join(e) for e in self.board]
        print('\n-----\n'.join(row))

    def winner(self):
        d, d1 = [], []

        for i in range(len(self.board)):

            d.append(self.board[i][i])
            d1.append(self.board[2 - i][i])

            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]  # по горизонтали

            elif self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]  # по вертикали

        if d[0] != ' ' and d[0] == d[1] == d[2]:  # по диагонали
            return d[0]

        elif d1[0] != ' ' and d1[0] == d1[1] == d1[2]:  # по другой диагонали
            return d1[0]

        elif not self.free_spaces():
            return 'Ничья'

    def free_spaces(self):
        return sum([e.count(' ') for e in self.board])

    def is_game_over(self):
        return self.winner() in (O, X) or not self.free_spaces()


while True:
    tictactoe = TicTacToe()
    print('Добро пожаловать в игру крестики-нолики')
    while not tictactoe.is_game_over():
        x, y = input(f'Ходит: {O if tictactoe.step else X}\nВведите X и Y: ').split(' ')
        tictactoe.mark(x, y)
        tictactoe.show()

    print('Победитель', tictactoe.winner())


