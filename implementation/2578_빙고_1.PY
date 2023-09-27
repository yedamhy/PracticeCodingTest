import sys

def input():
    return sys.stdin.readline().rstrip()


# 빙고가 있는지 확인하기
def check(bingo):
    count = 0
    # 가로 빙고 확인
    for bingo_row in bingo:
        if bingo_row.count(0) == 5:
            count += 1

    # 세로 빙고 확인
    for bingo_col in zip(*bingo):
        if bingo_col.count(0) == 5:
            count +=1

    # 대각선 1 확인 (왼쪽위 -> 오른쪽 아래)
    diagonal_cnt = 0
    for i in range(5):
        if bingo[i][i] == 0:
            diagonal_cnt += 1

    if diagonal_cnt == 5:
        count += 1

    # 대각선 2 확인 (오른쪽 위 -> 왼쪽 아래)
    diagonal_cnt = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            diagonal_cnt += 1

    if diagonal_cnt == 5:
        count += 1    

    if count == 3:
        return True
    else: return False


def main():
    """
    bingo = []
    for _ in range(5):
        bingo.append(list(map(int, input().split())))

    answer = []
    for _ in range(5):
        answer += (list(map(int, input().split())))
    """
    bingo = [
    [9, 10, 1, 11, 12],
    [13, 14, 2, 15, 16],
    [3, 4, 17, 5, 6],
    [18, 19, 7, 20, 21],
    [22, 23, 8, 24, 25]]

    answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    for num in answer:
        for bingo_row in bingo:
            if num in bingo_row:
                bingo[bingo.index(bingo_row)][bingo_row.index(num)] = 0
                print(bingo[0])
                print(bingo[1])
                print(bingo[2])
                print(bingo[3])
                print(bingo[4])
                print("----------------", answer.index(num)+1)
                if check(bingo):
                    print(answer.index(num) + 1)
                    return 



if __name__ == '__main__':
    main()