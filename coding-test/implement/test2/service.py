class Service:
    def __init__(self, n):
        self.n = n추천
        pass

    def __repr__(self):
        return f'{self.__class__}'

    def run(self):
        return self._three_count()

    def _three_count(self):
        count = 0
        for h in range(self.n + 1):
            for m in range(60):
                for s in range(60):
                    if '3' in f'{h}{m}{s}':
                        count += 1

        return count
