N = int(input())

for i in range(1, N+1):
    # 홀수 줄: 별부터 시작
    if i % 2 == 1:             
        print('* ' * N)
        
    # 짝수 줄: 공백부터 시작
    else:                      
        print(' ' + '* ' * N)