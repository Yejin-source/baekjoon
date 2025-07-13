# 문자열의 개수
N, M = map(int, input().split())

s_list = []
check_words = []

# N개의 줄: 집합 S에 포함되어 있는 문자열
for _ in range(N):
    s = input()
    s_list.append(s)

# M개의 줄: 검사해야 하는 문자열
for _ in range(M):
    word = input()
    check_words.append(word)


count = 0

# 문자열이 s에 포함되어 있는지 검사
for word in check_words:
    if word in s_list:
        count += 1

print(count)


# 보완할 점
# 탐색 성능 향상을 위한 set 사용

# s_list = set(input() for _ in range(N))
# check_words = [input() for _ in range(M)]