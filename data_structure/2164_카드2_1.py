import sys
from collections import deque
# 입력받기
def input():
    return sys.stdin.readline().rstrip()

#n = int(input())
n = 4

card = deque(range(n, 0, -1))

for _ in range(n-1):
    card.pop()
    card.appendleft(card.pop())

print(card[0])