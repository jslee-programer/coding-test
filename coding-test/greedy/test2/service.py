class Service:
    def __init__(self, f_input, s_input):
        self.condition = [int(x) for x in f_input.split(" ")]
        self.data = [int(x) for x in s_input.split(" ")]

    def __repr__(self):
        return f'{self.__class__}'

    def get_max_num(self):
        li = list(reversed(sorted(self.data)))
        n, m, k = self.condition
        remainder = m % k
        q = m // k
        result = li[0] * k * q
        if k < m:
            result += li[1] * remainder

        return result
