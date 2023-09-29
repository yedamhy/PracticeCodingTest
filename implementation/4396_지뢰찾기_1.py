import sys

def input():
    return sys.stdin.readline().rstrip()


# 자기 자리 숫자 찾기
def bomb_cnt(x, y):
    result = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if i == 0 and j == 0:
                    continue
                elif x+i < 0 or y+j < 0 :
                    continue 

                elif input1[x+i][y+j] == '*':
                    result += 1

            except IndexError:
                continue

    return result

def main():
    n = int(input())

    # 지뢰가 열렸는지 확인하기 위함
    bomb = 0
    global input1, input2


     # input1 입력 받기
    input1 = []
    for _ in range(n):
        input1.append(list(input()))

    # input2 입력 받기    
    input2 = []
    for _ in range(n):
        input2.append(list(input()))


    output = [[] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            # user가 누른 건지 확인
            if input2[x][y] == 'x':
                # 지뢰인지 확인
                if input1[x][y] == '*':
                    output[x].append('*') # check 되어 있는 output 다 돌고 + 지뢰칸도 열어줘야 함.
                    bomb += 1
                # 지뢰 아니면 숫자 
                elif input1[x][y] == '.':
                    output[x].append(bomb_cnt(x, y))

            # user 가 열지 않은 칸        
            else:
                output[x].append('.')

    if bomb > 0 :
        for x in range(n):
            for y in range(n):
                if input1[x][y] == '*':
                    output[x][y] = '*'

    for output_line in output:
        print(''.join(map(str, output_line)))

if __name__ == '__main__':
    main()        