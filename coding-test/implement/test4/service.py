#  각 맵의 칸은 (A, B) 로 나타낼 수 있다.
# A는 북쪽으로 부터 떨어진 칸의 개수
# B는 서쪽으로부터 떨어진 칸의 개수
# 현재방향 왼쪽부터 가보지 않은 칸이 있는지 탐색
# 네방향 모두 가보지 않은 칸이 존재하지 않는 경우나 바다로 되어있는 칸인 경우에는
# 바라보는 방향을 유지한 채로 한 칸 뒤로 간다.
# 다시 가보지 않는 칸이 있는지 탐색


class Service:
    # _TERRAIN = ((1, '바다'), (0, '육지'))
    # 0 = 북쪽, 1 = 동쪽, 2 = 남쪽, 3 = 서쪽
    # _VECTOR = ((0, (0, -1)), (1, (-1, 0)), (2, (0, 1)), (3, (1, 0)))
    _VECTOR = {
        0: (0, -1),
        1: (-1, 0),
        2: (0, 1),
        3: (1, 0),
    }

    def __init__(self, nm, current_location_vector, *args):
        _nm = nm.split(" ")
        self._map = self._make_map(_nm[0], _nm[1], args)
        self.current_location = tuple([int(x) for x in current_location_vector.split(" ")[:2]])
        self.direction = int(current_location_vector.split(" ")[2])
        pass

    def __repr__(self):
        return f'{self.__class__}'

    @staticmethod
    def _make_map(n, m, terrain):
        di = {}
        for y in range(int(n)):
            for x in range(int(m)):
                possible_locate = False if int(terrain[y].split(" ")[x]) == 1 else True
                di.setdefault((x, y), {}).update({
                    'pl': possible_locate,
                    'experience': possible_locate
                })

        print(di)
        return di

    def run(self):
        count = 1  # 방문한 횟수
        change_vector_count = 0  # 방향전환 횟수 체크
        while True:
            self._map[tuple(self.current_location)]['experience'] = False
            moving = self._VECTOR.get(self.direction)
            check_vector = tuple([self.current_location[0] + moving[0], self.current_location[1] + moving[1]])
            # 육지이고, 가본적이 없으면 이동
            if self.have_been(check_vector) and self.can_moving(check_vector):
                self.current_location = check_vector
                change_vector_count = 0
                count += 1
                continue
            # 4방향을 모두 돌았는데
            # 뒤로 갈수도 없으면
            # 가능한 경우의 수가 없으므로 멈춘다.
            elif change_vector_count == 4:
                # 뒤로 갈 수 있다
                # 이경우엔 육지 or 바다인지만 확인하면 됨
                check_vector = tuple([self.current_location[0] - moving[0], self.current_location[1] - moving[1]])
                if self.can_moving(check_vector):
                    change_vector_count = 0
                    self.current_location = check_vector
                    continue

                # 뒤로 갈수도 없으므로 BREAK
                break
            else:
                # 4방향을 아직 안돌았으므로
                # 방향전환
                change_vector_count = (change_vector_count + 1) % 5
                self.direction = self.direction + 1 if self.direction < 3 else 0
        return count

    # 현재 방향을 갈 수 있는지 없는지 확인
    # 육지 바다를 거르는 것
    def can_moving(self, check_vector):
        return self._map.get(check_vector)['pl']

    # 가본적 있는지
    def have_been(self, check_vector):
        return self._map.get(check_vector)['experience']
