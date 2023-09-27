import sys

def input():
    return sys.stdin.readline().rstrip()

count = 0

# 처음 소가 어디있는지 파악하기
def find_init_cow(cow): 
    init_cow = {}
    for c in cow:
        if c[0] not in init_cow:
            init_cow[c[0]] = c[1]

    return init_cow

# 소 위치가 바뀌는지 확인하기
# init_cow : 지금까지 cow의 위치 정보 나타내는 배열
# cow_num : cow 번호 , location : cow 현재 위치
def check_location(init_cow ,cow_num, location):
    # init_cow에서 소 찾기
    global count

    # 위치가 달라졌다면 바꿔주기
    if init_cow[cow_num] != location:
        init_cow[cow_num] = location
        count += 1

    return init_cow

def main():
    n = int(input())
    cow = []

    for _ in range(n):
        cow.append(list(map(int, input().split())))

    init_cow = find_init_cow(cow)
    
    for c , l in cow:
        init_cow = check_location(init_cow, c, l)

    print(count)

if __name__ == "__main__":
    main()