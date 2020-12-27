class Service:
    def __init__(self, n, moves):
        self.n = self._make_map(n)
        self.move_li = [move for move in moves.split(" ")]
        self.location = [1, 1]
        pass

    def __repr__(self):
        return f'{self.__class__}'

    @staticmethod
    def _make_map(n):
        li = list()
        for i in range(n):
            row = []
            for j in range(n):
                row.append([i + 1, j + 1])

            li.append(row)
        print(li)
        return li

    def run(self):
        for _, move in enumerate(self.move_li):
            if move == 'R':
                self._right_move()
            if move == 'L':
                self._left_move()
            if move == 'U':
                self._up_move()
            if move == 'D':
                self._down_move()

        return self.location

    def _current_location(self, row, column):
        row -= 1
        column -= 1

        if column < 0 or row < 0:
            print("좌표값을 벗어났습니다.")
            return self.location

        self.location = self.n[row][column]
        row, column = self.location
        return row, column

    def _left_move(self):
        row, column = self.location
        column -= 1
        self.location = list(self._current_location(row, column))
        pass

    def _right_move(self):
        row, column = self.location
        column += 1
        self.location = list(self._current_location(row, column))

    def _up_move(self):
        row, column = self.location
        row -= 1
        self.location = list(self._current_location(row, column))

    def _down_move(self):
        row, column = self.location
        row += 1
        self.location = list(self._current_location(row, column))
