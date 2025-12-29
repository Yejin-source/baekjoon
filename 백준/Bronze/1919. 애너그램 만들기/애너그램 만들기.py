a = input()
b = input()

a_cnt = [0] * 26
b_cnt = [0] * 26

# 첫 번째 문자열 문자 개수 세기
for ch in a:
    a_cnt[ord(ch) - ord('a')] += 1

# 두 번째 문자열 문자 개수 세기
for ch in b:
    b_cnt[ord(ch) - ord('a')] += 1

total = 0

# 애너그램이 되도록 삭제해야 하는 문자 수 계산
for i in range(26):
    total += abs(a_cnt[i] - b_cnt[i])

print(total)