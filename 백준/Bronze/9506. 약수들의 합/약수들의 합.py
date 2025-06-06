while True:
    num = int(input())
    
    if num == -1:  # 입력값이 -1인 경우
        break      # 반복 종료

    factors = []  # 약수 리스트


    # 1부터 num-1까지 반복
    for i in range(1, num):
        if num % i == 0:       # 나누어떨어지면 약수
            factors.append(i)  # 리스트에 추가

    # 약수의 합이 자신과 같다면 완전수
    if sum(factors) == num:
        # '6 = 1 + 2 + 3' 형태로 출력
        print(num, "=", " + ".join(str(i) for i in factors))

    else:
        # 완전수가 아닌 경우
        print(num, "is NOT perfect.")