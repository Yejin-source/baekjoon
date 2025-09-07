# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    sentence = input().split()

    # 각 단어를 모두 뒤집어서 출력
    for word in sentence:
        print(word[::-1], end=' ')
    print()  # 문장마다 줄바꿈


# 다른 풀이 (join)

# print(' '.join(word[::-1] for word in sentence))

# ' '.join(...)
# 리스트의 문자열을 하나로 합치기 (공백 구분)