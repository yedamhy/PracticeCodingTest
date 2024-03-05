# 백준 - 배열 실버5 "방 번호"
# 링크 : https://www.acmicpc.net/problem/1475

import sys
import math

def input():
    return sys.stdin.readline().rstrip()



def solution(room_number):
    numbers1 = ['0','1', '2', '3', '4', '5', '7', '8']

    max = 0
    for n in numbers1:
        if max <= room_number.count(n):
            max = room_number.count(n)

    numbers2_cnt = room_number.count('6') + room_number.count('9')
    if max <= math.ceil(numbers2_cnt/2):
        max = math.ceil(numbers2_cnt/2)

    return max

room_number = list(str(input()))
print(solution(room_number))
