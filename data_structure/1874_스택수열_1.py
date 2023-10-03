from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()

global result, stack, user

def stack_push(number):
    result.append('+')
    stack.append(number)


def stack_pop():
    result.append('-')
    stack.pop()
   
# 결과 출력 result
result = []

# 1부터 n까지 수열
# n 은 입력 받음
n = int(input())
sequence = [a + 1 for a in range(n)]

user = deque()

for _ in range(n):
    user.append(int(input()))

stack = deque()
error = 0
while(user):
    try:
        now = user.popleft()
        if len(stack) == 0:
            stack_push(sequence[0])
            del sequence[0]

        if stack[-1] != now:
            stack_push(sequence[0])
            user.appendleft(now)
            del sequence[0]

        else:
            stack_pop()

    except IndexError:
        error += 1

if error > 0:
    print("NO")

else:
    for plus_minus in result:
        print(plus_minus)

