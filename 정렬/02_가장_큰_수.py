# 프로그래머스 "알고리즘 고득점 kit - 정렬" LEVEL2
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = [str(num) for num in numbers]

    # 문자열을 연결했을 때 사전순 내림차순
    # 문자열 길이가 1000이하이니깐 x*3, if 100이하이면 x*2
    numbers.sort(key=lambda x: x*3, reverse=True)

    result = ''.join(numbers)

    # 모든 숫자가 0인 경우를 처리 (예: [0, 0, 0] -> '0')
    return str(int(result))
