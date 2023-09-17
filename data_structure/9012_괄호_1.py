import sys

def input():
    return sys.stdin.readline().rstrip()

result_list = []

# 몇 줄 입력 받을지 입력받기
n = int(input())

for i in range(n):
    s = list(input())
    result = ''
    cnt = 0
    for c in s:
        if c == '(':
            cnt +=1
        elif c == ')':
            cnt -= 1

        if cnt < 0:
            result = 'NO'
            break

    if result == '' and cnt == 0:
        result = 'YES'
    else:
        result = 'NO'

    result_list.append(result)

for i in range(n):
    print(result_list[i])