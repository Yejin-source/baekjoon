vowels = 'aeiouAEIOU'  # 모음

while True:
    sentence = input()
    
    if sentence == '#':  # 종료 조건
        break

    count = 0  # 모음 개수

    for ch in sentence:   # 한 글자씩 순회
        if ch in vowels:  # 모음이면
            count += 1    # 개수 증가

    print(count)