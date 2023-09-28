import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def test_case_printer(now_location, print_que):
    out_order = 0
    while(print_que):
        now_max = max(print_que)

        temp_num = print_que.popleft()
        if now_max == temp_num:
            out_order += 1
            if now_location == 0:
                break
        else:
            print_que.append(temp_num)

        # 현재 문서 위치 파악
        now_location -= 1
        if now_location < 0:
            now_location = len(print_que) - 1

    print(out_order)

def main():
    n = int(input())
    for _ in range(n):        
        print_que = deque()
        a, now_location = map(int, input().split())
        print_list = list(map(int, input().split()))

        for n in print_list:
            print_que.append(n)

        test_case_printer(now_location, print_que)

if __name__ == '__main__':
    main()