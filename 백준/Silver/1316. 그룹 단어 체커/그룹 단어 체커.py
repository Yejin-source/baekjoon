# 단어의 개수
N = int(input())

# 모든 단어가 그룹 단어라고 가정
count = N

# N번 반복
for _ in range(N):
    word = input()

    # 단어의 각 문자를 순서대로 확인
    for i in range(0, len(word)-1):

        # 문자가 연속해서 나타나는 경우
        if word[i] == word[i+1]:
            pass  # 그냥 다음 문자로 넘어감

        # 문자가 떨어져서 나타나는 경우
        elif word[i] in word[i+1:]: # 현재 문자가 이후의 문자열에 나오는지 확인
            count -= 1  # 그룹 단어 개수 감소
            break       # 반복 종료

# 최종 그룹 단어 개수 출력
print(count)

