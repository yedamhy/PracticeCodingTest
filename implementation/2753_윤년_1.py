import sys

def input():
    return sys.stdin.readline().rstrip()

def leap_year(year):
    if (year % 4 == 0 and year%100 != 0) or year % 400 == 0:
        return 1
    else:
        return 0
    
year = int(input())
print(leap_year(year))