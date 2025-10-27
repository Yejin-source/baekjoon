while True:
    A, B = map(int, input().split())  # 두 정수
    
    if A == 0 and B == 0:  # 종료 조건
        break
    
    # 평균과 중앙값을 같게 만드는 가장 작은 정수 출력
    print(2*A-B)