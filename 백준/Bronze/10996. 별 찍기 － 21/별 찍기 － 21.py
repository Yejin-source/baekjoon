N = int(input())

for i in range(2*N):  # 총 2N줄
    
    # 홀수 줄: '* ' 패턴
    if i % 2 == 0:   
        print('* ' * ((N+1) // 2))
        
    # 짝수 줄: ' *' * 패턴
    else:             
        print(' *' * (N // 2))