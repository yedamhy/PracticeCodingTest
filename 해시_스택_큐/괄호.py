# 백준 실버4
# 링크 : https://www.acmicpc.net/problem/9012

from collections import deque 
import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(ps_list):
    queue = deque()
    for s in ps_list:
        if s == "(":
            queue.append(s)
        elif len(queue) < 1:
            return "NO"
        elif queue.popleft() == "(":
            continue
        else:
            return "NO"

    if len(queue) > 0:
        return "NO"

    return "YES"

def result():
    n = int(input())

    for _ in range(n):
        ps_list = list(input())
        print(solution(ps_list))

result()
