word = input()

# 크로아티아 알파벳 저장
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


for ch in croatia:
    # 크로아티아 알파벳을 별로 대체
    word = word.replace(ch, "*")

# 바뀐 문자열의 길이 == 글자 수
print(len(word))