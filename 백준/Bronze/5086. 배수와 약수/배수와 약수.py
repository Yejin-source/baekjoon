while True:
    a, b = map(int, input().split())
    
    # 입력이 0 0인 경우 반복 종료
    if a == 0 and b == 0:
        break
    
    # a가 b의 약수라면
    if b % a == 0:
        print("factor")
    
    # a가 b의 배수라면
    elif a % b == 0:
        print("multiple")
        
    # 둘 다 아니라면
    else:
        print("neither")