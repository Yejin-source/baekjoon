# 세 각을 리스트로 저장
angles = [int(input()) for _ in range(3)]

# 세 각의 합이 180이 아닌 경우
if sum(angles) != 180:
    print('Error')

# 세 각의 크기가 모두 60인 경우 (세 각이 모두 같은 경우)
elif angles.count(angles[0]) == 3:
    print('Equilateral')

# 두 각이 같은 경우
elif len(set(angles)) == 2:  # set()으로 중복 제거 후
    print("Isosceles")       # len()으로 서로 다른 값 개수 확인

# 세 각이 모두 다른 경우
else:
    print('Scalene')


# 초기 시도한 코드 -> 더 깔끔하게 다듬기 위해 재도전

# first = int(input())
# second = int(input())
# third = int(input())

# if first + second + third == 180:
#     if first == second == third:
#         print('Equilateral')
#     elif first == second or second == third or first == third:
#         print('Isosceles')
#     else:
#         print('Scalene')
# else:
#     print('Error')