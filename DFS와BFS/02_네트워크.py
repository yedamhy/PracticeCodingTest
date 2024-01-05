# 프로그래머스 "알고리즘 고득점 kit" LEVEL3
# 링크 : https://github.com/yedamhy/CodingTestPractice

def dfs(computers, v, check):
    computer_link = computers[v]
    # 방문 표시
    check[v] = True
    computer_link[v] = 0
    
    while(1 in computer_link):
        # 방문할 노드 선정
        v = computer_link.index(1)
        
        computer_link[v] = 0
        dfs(computers, v, check)

def solution(n, computers):
    answer = 0
    check = [False] * n
    
    while(False in check):
        v = check.index(False)
        dfs(computers, v, check)
        answer += 1
    
    return answer
