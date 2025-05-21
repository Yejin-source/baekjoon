# 알파벳 대문자 단어
word = input()

min_time = 0

# 단어 한 글자씩 반복
for ch in word:
    # 알파벳에 따라 '해당 숫자 +1'만큼 시간 추가
    if ch in 'ABC':
        min_time += 3  # (2+1)초
    elif ch in 'DEF':
        min_time += 4
    elif ch in 'GHI':
        min_time += 5
    elif ch in 'JKL':
        min_time += 6
    elif ch in 'MNO':
        min_time += 7
    elif ch in 'PQRS':
        min_time += 8
    elif ch in 'TUV':
        min_time += 9
    elif ch in 'WXYZ':
        min_time += 10

# 전화를 거는 최소 시간
print(min_time)