import sys

# input으로 주어질 것.
# 현금
# 1일차 ~ 14일차 주식 가격
# output
# 가진 주식 수, 남은 현금

def input():
    return sys.stdin.readline().rstrip()


def bnf(cash, price_list):
    buy = 0
    for price in price_list:
        if cash >= price:
            buy = cash // price
            cash -= price * buy
    
    return cash + buy * price_list[-1]   


def timing(cash, price_list):
    buy = 0
    
    for i in range(2, len(price_list)):
        # 매도 타이밍
        if (price_list[i] > price_list[i-1] > price_list[i-2] > price_list[i-3]
            ) and buy != 0:
            today_sell = buy * price_list[i]
            cash += today_sell
            buy = 0

    # 매수타이밍
        today_buy = 0
        if (price_list[i] < price_list[i-1] < price_list[i-2] <price_list[i-3]
            ) and cash >= price_list[i] :
            today_buy = cash // price_list[i] 
            cash -= price_list[i] * today_buy

            buy += today_buy

    return cash + buy * price_list[-1]   

def main():
    cash = int(input())
    price_list = list(map(int, input().split()))

    bnf_price = bnf(cash, price_list)
    timing_price = timing(cash, price_list)

    if bnf_price > timing_price:
        print('BNP')
    
    elif bnf_price == timing_price:
        print('SAMESAME')

    else: print('TIMING')

if __name__ ==  '__main__':
    main()