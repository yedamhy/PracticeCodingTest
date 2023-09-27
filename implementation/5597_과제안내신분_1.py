import sys

# 입력 받기
def input():
    return sys.stdin.readline().rstrip()

# 30명 출석부 만들기
student = []
for i in range(30):
    student.append(i+1)

# 출석한 사람 제거
for _ in range(28):
    attend = int(input())
    student.remove(attend)

print(student[0])
print(student[-1])