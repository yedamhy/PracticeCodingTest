'''
import sys
import re

def input():
    return sys.stdin.readline().rstrip()

def queue(s, que):
    # 기능1. push X
    if s.startswith('push'):
        num = int(s.split()[1]) # num = int(s.split()[1])
        que.append(num)

    # 기능2. pop
    if s == 'pop':
        if len(que) == 0:
            print(-1)

        else:
            print(que[0])
            que.pop()

    # 기능3. size 
    if s == 'size':
        print(len(que))
    
    # 기능4. empty
    if s == 'empty':
        if len(que) <= 0:
            print(1)
        else : 
            print(0)
        
    # 기능5. front
    if s == 'front':
        if len(que) <= 0:
            print(-1)
        else:
            print(que[0])
        
    # 기능6. back
    if s == 'back':
        if len(que) <= 0:
            print(-1)
        else:
            print(que[-1])    



n = int(input())
q = []
for i in range(n):
    s = input()
    queue(s, q)
'''
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def queue(s, que):
    # 기능1. push X
    if s.startswith('push'):
        num = int(s.split()[1])
        que.append(num)

    # 기능2. pop
    elif s == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())  # 큐에서 맨 앞 요소를 제거하고 출력

    # 기능3. size 
    elif s == 'size':
        print(len(que))
    
    # 기능4. empty
    elif s == 'empty':
        if len(que) <= 0:
            print(1)
        else : 
            print(0)
        
    # 기능5. front
    elif s == 'front':
        if len(que) <= 0:
            print(-1)
        else:
            print(que[0])
        
    # 기능6. back
    elif s == 'back':
        if len(que) <= 0:
            print(-1)
        else:
            print(que[-1])    

n = int(input())
que = deque()  # que 변수를 정의
for i in range(n):
    s = input()
    queue(s, que)
