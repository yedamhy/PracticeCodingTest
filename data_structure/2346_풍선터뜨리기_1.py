import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    
    # 풍선, 쪽지 디큐 만들기
    input_message = list(map(int, input().split()))
    
    balloon = deque()
    message = deque()
    for i in range(n):
        balloon.append(i+1)
        message.append(input_message[i])

    # 1번 풍선 터뜨리기
    output = []
    output.append(balloon.popleft())
    move = message.popleft()

    while(balloon):
        if move > 0:
            for _ in range(abs(move)):

                # deque에서 꺼내
                temp_output_balloon = balloon.popleft()
                temp_output_message = message.popleft()

                #deque에 다시 집어넣어
                balloon.append(temp_output_balloon)
                message.append(temp_output_message)
            
            output.append(balloon.pop())
            move = message.pop() 

        
        else:
            for _ in range(abs(move)):
                # deque에서 꺼내
                temp_output_balloon = balloon.pop()
                temp_output_message = message.pop()

                #deque에 다시 집어넣어
                balloon.appendleft(temp_output_balloon)
                message.appendleft(temp_output_message)

            output.append(balloon.popleft())
            move = message.popleft() 

    print(' '.join(map(str, output)))

if __name__ == '__main__':
    main()