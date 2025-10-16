T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    mars = input().split()
    num = float(mars[0])  # 첫 번째 값은 숫자

    # 그 다음에는 연산자에 따라 계산
    for m in mars[1:]:
        if m == '@':
            num *= 3
        elif m == '%':
            num += 5
        elif m == '#':
            num -= 7
            
    print("%.2f" % num)  # 포맷 스트링 사용