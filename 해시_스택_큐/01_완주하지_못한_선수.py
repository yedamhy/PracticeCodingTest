# 프로그래머스 알고리즘 고득점 KIT LEVEL1
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    name_list = {}
    for p in participant:
        if p in name_list:
            name_list[p] += 1
        else:
            name_list[p] = 1
    
    # 완주자
    for c in completion:
        name_list[c] -= 1
        
    # 완주 못한 사람 기준
    for person in name_list:
        if name_list[person] > 0 :
            answer = person
            
    return answer
