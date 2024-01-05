# 프로그래머스 "알고리즘 고득점 KIT" LEVEL2
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    queue = deque([0])

    for n in numbers:
        for _ in range(len(queue)):
            v = queue.popleft()
            
            queue.append(v+n)
            queue.append(v-n)
                
    return queue.count(target)
