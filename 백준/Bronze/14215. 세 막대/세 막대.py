# 세 막대의 길이를 오름차순으로 정렬
sides = sorted(map(int, input().split()))


# 가장 긴 막대 < 나머지 두 막대의 합 -> 삼각형의 조건 만족
if sides[2] < sides[0] + sides[1]:
    print(sum(sides))  # 세 막대의 합 = 삼각형의 둘레

    
# 삼각형이 될 수 없는 경우 -> 가장 긴 막대를 줄여서 만들 수 있는 최대 둘레 계산   
else:
    # 둘레 = 짧은 두 변의 합 * 2 - 1 (삼각형 조건을 만족하기 위한 최대값)
    print((sides[0] + sides[1]) * 2 - 1)
    
    
# sorted() vs sort()
# sorted(): 정렬된 새 리스트를 반환 (원본 그대로)
# sort(): 리스트 자체를 정렬 (원본 변경, 반환값 X)