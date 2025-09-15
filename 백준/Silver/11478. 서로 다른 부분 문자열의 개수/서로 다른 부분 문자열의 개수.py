S = input()  # 문자열

substrings = []

for i in range(len(S)):             # 슬라이싱 시작 위치
    for j in range(i+1, len(S)+1):  # 슬라이싱 끝 위치
        substrings.append(S[i:j])

# 중복 제거 후 출력
print(len(set(substrings)))