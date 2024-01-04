# 프로그래머스 "알고리즘 고득점 kit - 정렬"
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations = sorted(citations)
    answer = 0
    
    for i in range(len(citations)):
        check_list = citations[i:]
        
        if len(check_list) >= citations[i]:
            h_index = citations[i]
        
        else: 
            h_index = len(check_list)

        answer = h_index if answer < h_index else answer
    
    return answer
