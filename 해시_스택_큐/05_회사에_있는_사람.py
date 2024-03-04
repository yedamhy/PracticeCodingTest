# 백준 해시 - 실버5 "회사에 있는 사람"
# 링크 : https://www.acmicpc.net/problem/7785

import sys

def input():
    return sys.stdin.readline().rstrip()


def result():
    n = int(input())

    log_dict = {}

    for _ in range(n):
        working = list(input().split(' '))
        if working[1] == 'enter':
            log_dict[working[0]] = 1
        elif working[1] == 'leave':
            del log_dict[working[0]]

    result_names= []
    for name in log_dict:
        result_names.append(name)
        
    result_names = sorted(result_names)  
    for name in result_names[::-1]:
        print(name)


result()
