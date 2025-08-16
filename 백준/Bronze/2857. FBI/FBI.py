# 개선 코드: 언패킹 사용

found = []  # FBI 요원 리스트

for i in range(1, 6):
    code = input()  # 요원 코드

    if 'FBI' in code:
        found.append(i)

# *리스트 -> 언패킹: 리스트 원소를 낱개로 풀어 공백 구분 출력
# found가 비어있으면 'HE GOT AWAY!' 출력
print(*found if found else ['HE GOT AWAY!'])


# 이전 코드

# if found:
#     for idx in found:
#         print(idx, end=' ')
# else:
#     print('HE GOT AWAY!')