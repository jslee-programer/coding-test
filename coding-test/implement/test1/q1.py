from implement.test1.service import Service

if __name__ == '__main__':
    sv = Service(6, "R R R R R R D D D D L L U L L L")
    print(sv.__repr__())
    print(sv.run())
