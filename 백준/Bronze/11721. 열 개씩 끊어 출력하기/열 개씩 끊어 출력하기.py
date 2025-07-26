word = input()

for i in range(0, len(word), 10):  # 10글자씩 끊어서 출력
    print(word[i:i+10])