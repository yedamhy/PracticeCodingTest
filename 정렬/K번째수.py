# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42748

# merge 정렬
def sorting(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = sorting(arr[:mid])
    right_half = sorting(arr[mid:])
    
    i, j = 0, 0
    sorted_arr = []
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
            
        else:
            sorted_arr.append(right_half[j])
            j += 1

    while i < len(left_half):
        sorted_arr.append(left_half[i])
        i += 1 
            
    while j < len(right_half):
        sorted_arr.append(right_half[j])
        j += 1 
        
    return sorted_arr

def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[command[0] -1 : command[1]]
        sorted_arr = sorted(arr)

        answer.append(sorted_arr[command[2]-1])
    return answer
