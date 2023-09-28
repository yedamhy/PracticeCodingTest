import sys

def input():
    return sys.stdin.readline().rstrip()

balloon = [[1, 3],
           [2, 2],
           [3, 1],
           [4, -3],
           [5, -1]]

output = []

# 첫번째 풍선 터뜨리기
output.append(1)
moving_num = balloon[0][1]
balloon[0][[0]], balloon[0][1] = 0, 0

while(balloon):
    if balloon[moving_num][0] != 0:
        # 터뜨린 풍선 번호 추가
        output.append([moving_num][0])
        moving_num += balloon[]
        balloon[moving_num][[0]], balloon[moving_num][1] = 0, 0


    else:
        moving_num += 1
