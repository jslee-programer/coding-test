from implement.test1.service import Service

if __name__ == '__main__':
    sv = Service(5, "R R R R U D D")
    print(sv.__repr__())
    print(sv.run())
