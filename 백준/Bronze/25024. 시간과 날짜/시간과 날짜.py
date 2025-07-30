# 테스트 케이스 개수
T = int(input())

# 가독성 개선한 코드
for _ in range(T):
    x, y = map(int, input().split())

    # 시간 유효성 검사
    time_valid = 0 <= x <= 23 and 0 <= y <= 59

    # 날짜 유효성 검사
    if x in (1, 3, 5, 7, 8, 10, 12):
        date_valid = 1 <= y <= 31
    elif x in (4, 6, 9, 11):
        date_valid = 1 <= y <= 30
    elif x == 2:
        date_valid = 1 <= y <= 29
    else:
        date_valid = False

    # 검사 결과 출력 (삼항 연산자)
    print('Yes' if time_valid else 'No', end=' ')
    print('Yes' if date_valid else 'No')


# 처음 작성한 코드

# for _ in range(T):
#     x, y = map(int, input().split())

      # 시간 유효성 검사
#     if x >= 0 and x <= 23:
#         if y >= 0 and y <= 59:
#             print('Yes', end=' ')
#         else:
#             print('No', end=' ')
#     else:
#         print('No', end=' ')

      # 날짜 유효성 검사
#     if x in (1, 3, 5, 7, 8, 10, 12) and (y >= 1 and y <= 31):
#         print('Yes')
#     elif x in (4, 6, 9, 11) and (y >= 1 and y <= 30):
#         print('Yes')
#     elif x == 2 and (y >= 1 and y <= 29):
#         print('Yes')
#     else:
#         print('No')