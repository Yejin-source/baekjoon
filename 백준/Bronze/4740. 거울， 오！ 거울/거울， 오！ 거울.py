while True:
    sentence = input()

    if sentence == "***":
        break

    print(sentence[::-1])  # 문장 역순 출력