while True:
    a,b,c = map(int, input().split())
    sides = [a, b, c]

    # 세 변이 모두 0인 경우
    if sum(sides) == 0:
        break  # 반복 종료
    
    
    # 삼각형의 조건을 만족하지 못하는 경우 (가장 긴 변 >= 나머지 두 변의 합)
    if max(sides) >= sum(sides) - max(sides):
        print('Invalid')
    
    # 세 변의 길이가 모두 같은 경우
    elif len(set(sides)) == 1:
        print('Equilateral')
        
    # 두 변의 길이만 같은 경우
    elif len(set(sides)) == 2:
        print('Isosceles')
        
    # 세 변의 길이가 모두 다른 경우
    else:
        print('Scalene')