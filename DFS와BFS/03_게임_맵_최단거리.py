# 프로그래머스 고득점 알고리즘 KIT DFS와BFS LEVEL2
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    # 초기 설정
    queue = deque([(0, 0, 1)])
    # 방향 이동 설정 동, 서, 남, 북 순..
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        # 현재위치, 지난 칸 개수
        x, y, dist = queue.popleft()
        #print("현재 위치 : ", x, y)
        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 방문표시
                maps[nx][ny] = 0
                queue.append((nx, ny, dist+1))
        
    return -1
        
