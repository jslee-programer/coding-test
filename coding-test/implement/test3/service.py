class Service:
    HOR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    VER = ['1', '2', '3', '4', '5', '6', '7', '8']
    STEPS = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    LIMIT_MAX = 8
    LIMIT_MIN = 1

    def __init__(self, current_loc):
        self.current_loc = [current_loc[0], current_loc[1]]
        print(self.current_loc)

    def __repr__(self):
        return f'{self.__class__}'

    def run(self):
        hor_, ver_ = self.current_loc
        count = 0
        check_h = 0
        check_v = 0
        for i, h in enumerate(self.HOR, 1):
            if hor_ in h:
                check_h = i
                break

        for i, v in enumerate(self.VER, 1):
            if ver_ in v:
                check_v = i
                break

        for sh, sv in self.STEPS:
            if check_h + sh >= self.LIMIT_MIN and check_h + sv <= self.LIMIT_MAX and check_v + sv >= self.LIMIT_MIN and check_v + sv <= self.LIMIT_MAX:
                count += 1

        return count
