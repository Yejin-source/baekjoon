burger = min(int(input()) for _ in range(3))
drink = min(int(input()) for _ in range(2))

# 가장 싼 세트 메뉴 가격 출력
print(burger + drink - 50)