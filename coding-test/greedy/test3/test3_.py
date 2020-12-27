from greedy.test3 import service

if __name__ == '__main__':
    sv = service.Service("3 3", "3 1 2", "4 1 4", "2 2 2")
    print(sv.run())
