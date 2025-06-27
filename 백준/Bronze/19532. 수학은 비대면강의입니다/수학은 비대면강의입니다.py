a, b, c, d, e, f = map(int, input().split())

found = False  # 해를 찾았는지 여부

# x, y는 각각 -999 이상 999 이하의 정수만 허용
for x in range(-999, 1000):
    for y in range(-999, 1000):
        
        # 두 식을 모두 만족하는 경우
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)   # 해 출력
            found = True
            break         # 내부 반복 종료
        
    if found:  # found = True 와 같음
        break  # 외부 반복 종료