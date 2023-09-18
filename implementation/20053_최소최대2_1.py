import sys

def input():
    return sys.stdin.readline().rstrip()

def min_max(num_list, n):
    for i in range(n):
        num_list[i] = int(num_list[i])
    return print(min(num_list), max(num_list))

n = int(input())

for _ in range(n):
    length = int(input())

    # 입력 받은 걸 list에 저장
    num_string = input()
    num_list = num_string.split(' ')

    min_max(num_list, length)