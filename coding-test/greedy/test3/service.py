class Service:
    def __init__(self, *args):
        self.args = args
        pass

    def __repr__(self):
        return f'{self.__class__}'

    def run(self):
        print(len(self.args))
        li = []
        for _, x in enumerate(self.args[1:]):
            li.append(min([int(x) for x in x.split(" ")]))

        print(li)
        return max(li)
