from collections import deque

from dfs_bfs.test1.service import Service

if __name__ == '__main__':
    # 스택
    st = list()
    st.append(5)
    st.append(2)
    st.append(3)
    st.append(7)
    st.pop()
    st.append(1)
    st.append(4)
    st.pop()
    print(st)
    print(st[::-1])

    # 큐
    que = deque()
    que.append(5)
    que.append(2)
    que.append(3)
    que.append(7)
    que.popleft()
    que.append(1)
    que.append(4)
    que.popleft()

    print(que)
    que.reverse()
    print(que)

    sv = Service()
    print(sv.recursive_fn(1))
    print(f'반복적으로 구현: {sv.factorial_iterative(5)}')
    print(f'재귀적으로 구현: {sv.factorial_recursive(5)}')
