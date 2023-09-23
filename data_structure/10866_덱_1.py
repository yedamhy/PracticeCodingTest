import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def push(now_deque, comment):
    if 'front' in comment:
        now_deque.appendleft(int(comment.split()[1]))

    elif 'back' in comment:
        now_deque.append(int(comment.split()[1]))


    return now_deque

def pop(now_deque, comment):
    if len(now_deque) == 0:
        print(-1)

    elif 'front' in comment:
        print(now_deque.popleft())

    elif 'back' in comment:
        print(now_deque.pop())

    return now_deque

def size(now_deque):
    print(len(now_deque))
    return now_deque

def empty(now_deque):
    if len(now_deque) == 0:
        print(1)

    else:
        print(0)

def front(now_deque):
    if len(now_deque) == 0:
        print(-1)
    else:
        print(now_deque[0])

    return now_deque

def back(now_deque):
    if len(now_deque) == 0:
        print(-1)

    else:
        print(now_deque[-1])

    return now_deque

def main():
    n = int(input())
    now_deque = deque()

    for _ in range(n):
        comment = input()

        if 'push' in comment:
            now_deque = push(now_deque, comment)

        elif 'pop' in comment:
            now_deque = pop(now_deque, comment)

        elif comment == 'size':
            now_deque = size(now_deque)

        elif comment == 'empty':
            now_deque = empty(comment)

        elif comment == 'front':
            now_deque = front(comment)

        elif comment == 'back':
            now_deque = back(comment)


if __name__ == '__main__':
    main()
