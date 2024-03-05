# 백준 - 배열 : 브론즈2 "숫자의 개수"
# 링크 : https://www.acmicpc.net/problem/2577

import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    input_num = []
    for _ in range(3):
        input_num.append(int(input()))
    result = list(str(input_num[0]*input_num[1]*input_num[2]))
    
    numbers = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9']

    for n in numbers:
        print(result.count(n))

solution()
