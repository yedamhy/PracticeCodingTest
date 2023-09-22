import sys

def input():
    return sys.stdin.readline().rstrip()

# 1번 명령어
def first_command(i, x, now_bulb):
    if now_bulb[i-1] == 0:
        now_bulb[i-1] = 1

    else: now_bulb[i-1] = 0

    return now_bulb

# 2번 명령어
def second_command(l, r, now_bulb):
    for i in range(l, r+1):
        if now_bulb[i-1] == 0:
            now_bulb[i-1] = 1

        else: now_bulb[i-1] = 0

    return now_bulb

# 3번 명령어 
def third_command(l, r, now_bulb):
    for i in range(l, r+1):
        if now_bulb[i-1] == 1:
            now_bulb[i-1] = 0

    return now_bulb

# 4번 명령어
def fourth_command(l, r, now_bulb):
    for i in range(l, r+1):
        if now_bulb[i-1] == 0:
            now_bulb[i-1] = 1

    return now_bulb

# 제어 찾아주기
def find_command(a, iorl, xorr, now_bulb):
    if a == 1:
        first_command(iorl, xorr, now_bulb)

    if a == 2:
        second_command(iorl, xorr, now_bulb)
    
    if a == 3:
        third_command(iorl, xorr, now_bulb)

    if a == 4:
        fourth_command(iorl, xorr, now_bulb)  

    return now_bulb 


def main():
  num_bulb, num_command = map(int, input().split(' '))
  # 전구 상태 입력 받기
  now_bulb = list(map(int, input().split()))

  # 명령 실행
  for _ in range(num_command):
      a, iorl, xorr = map(int, input().split())
      now_bulb = find_command(a, iorl, xorr, now_bulb)

  print(*now_bulb) 

if __name__ == "__main__":
    main()