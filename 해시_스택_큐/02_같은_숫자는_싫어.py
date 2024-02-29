# 프로그래머스 "알고리즘 고득점 kit - 스택/큐" LEVEL1
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque

def solution(arr):
    answer = []
    
    # 첫번째 값은 넣어두고 시작
    answer.append(arr[0])
    for i in arr[1:]:
        if answer[-1] != i:
            answer.append(i)
            
    return answer
