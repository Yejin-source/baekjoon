N = int(input())

for i in range(N):
    sentence = input()

    # 첫 글자를 대문자로 바꾼 뒤 출력
    print(sentence[0].upper() + sentence[1:])