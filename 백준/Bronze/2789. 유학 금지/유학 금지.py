word = input()

ban = 'CAMBRIDGE'  # 검열할 알파벳

result = ''

for ch in word:
    if ch not in ban:  # 검열 알파벳에 포함되지 않으면
        result += ch   # 문자열에 추가

print(result)


# 다른 풀이 (join)

# print(''.join([ch for ch in word if ch not in ban]))