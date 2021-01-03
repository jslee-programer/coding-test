class Service:
    # >>>> 답지 보고 추가1>>>>
    MOVE_TYPES = ('R', 'L', 'U', 'D',)

    def __init__(self, n, moves):
        self.n = self._make_map(n)
        self.move_li = [move for move in moves.split(" ")]
        self.location = [1, 1]
        self.move_fn = (self._right_move, self._left_move, self._up_move, self._down_move,)
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
            for i, move_type in enumerate(self.MOVE_TYPES):
                if move_type == move:
                    self.move_fn[i]()
                    continue

        return self.location

    def _current_location(self, row, column):
        row -= 1
        column -= 1
        limit = len(self.n) - 1
        if not (limit >= column >= 0 and limit >= row >= 0):
            print(row, column)
            print(self.location)
            print("좌표값을 벗어났습니다.")
            return self.location

        self.location = self.n[row][column]

    def _left_move(self):
        row, column = self.location
        column -= 1
        self._current_location(row, column)

    def _right_move(self):
        row, column = self.location
        column += 1
        self._current_location(row, column)

    def _up_move(self):
        row, column = self.location
        row -= 1
        self._current_location(row, column)

    def _down_move(self):
        row, column = self.location
        row += 1
        self._current_location(row, column)
