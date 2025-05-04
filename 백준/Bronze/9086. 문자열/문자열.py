num = int(input())

for _ in range(num):
    text = input()
    # 문자열끼리 더해서 이어 붙이기
    print(text[0] + text[-1])  # 첫 글자 + 마지막 글자