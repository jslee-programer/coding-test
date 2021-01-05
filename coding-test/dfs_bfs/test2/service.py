from collections import deque


class Service:
    INF = 9999999999

    def __init__(self):
        pass

    def __repr__(self):
        pass

    # 인접 행렬
    # 2차원 배열로 그래프의 연결 관계를 표현하는 방식
    def adjacency_matrix(self):
        # graph = [
        #     [0, 7, 5],
        #     [7, 0, self.INF],
        #     [5, self.INF, 0]
        # ]

        graph = [
            [],  # 0번 노드
            [2, 3, 8],  # 1번 노드
            [1, 7],  # 2번 노드
            [1, 4, 5],  # 3번 노드
            [3, 5],  # 4번 노드
            [3, 4],  # 5번 노드
            [7],  # 6번 노드
            [2, 6, 8],  # 7번 노드
            [1, 7],  # 8번 노드
        ]

        return graph

    @staticmethod
    def adjacency_list():
        # 행이 3개인 2차원 리스트로 인접 리스트 표현
        graph = [[] for _ in range(3)]

        # 노드 0에 연결된 노드 정보 저장(노드, 거리)
        graph[0].append((1, 7))
        graph[0].append((2, 5))

        # 노드 1에 연결된 노드 정보 저장(노드, 거리)
        graph[1].append((0, 7))

        # 노드 2에 연결된 노드 정보 저장(노드, 거리)
        graph[2].append((0, 5))

        return graph

    # 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
    def dfs(self, graph, v, visited):
        # 현재 노드를 방문 처리
        # print(visited)
        visited[v] = True
        print(v, end=' ')
        # print(graph[v])
        # print(visited[v])
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                self.dfs(graph, i, visited)

    # 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘
    def bfs(self, graph, start, visited):
        # 큐(Queue) 구현을 위해 deque 라이브러리 사용
        queue = deque([start])
        print(queue)
        # 현재 노드를 방문 처리
        visited[start] = True
        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 하나의 원소를 뽑아 출력
            v = queue.popleft()
            print(v, end=' ')
            # 해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
