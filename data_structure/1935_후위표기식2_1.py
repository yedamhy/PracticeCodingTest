import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

def multi(num1, num2):
  return num1 * num2

def div(num1, num2):
  return float(num1 / num2)

def plus(num1, num2):
  return num1 + num2

def minus(num1, num2):
  return num1 - num2

def main():
  # 입력 받기
  n = int(input())

  cal_str = list(input())
  num_list = []
  for _ in range(n):
    num_list.append(int(input()))


  cal = deque()

  for l in cal_str:
    if l not in ['+', '-', '*', '/']:
      cal.append(num_list[ord(l) - ord('A')])

    else:
      num2 = cal.pop() 
      num1 = cal.pop()

      if l == '*':
        number_cal = multi(num1, num2)

      elif l == '/':
        number_cal = div(num1, num2)

      elif l == '+':
        number_cal = plus(num1, num2)

      elif l == '-':
        number_cal = minus(num1, num2)

      
      cal.append(number_cal)

  print(format(cal[0], '.2f'))

if __name__ == '__main__':
    main()
