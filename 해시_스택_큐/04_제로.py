# 백준 실버4 - 큐
# 링크 : https://www.acmicpc.net/problem/10773

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def solution(numbers):
    queue = deque()
    for n in numbers:
        if n == 0:
            queue.pop()
        else:
            queue.append(n)

    return sum(queue)

def result():
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))

    return solution(numbers)

print(result())
