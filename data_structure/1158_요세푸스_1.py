import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split(" "))

# deque 만들기
from collections import deque
yosefuse = deque(range(1, n+1))
result = []
while(yosefuse):
    for _ in range(k-1):
        yosefuse.append(yosefuse.popleft())

    result.append(yosefuse.popleft())

# 결과 출력
print("<" + ", ".join(map(str, result)) + ">")


