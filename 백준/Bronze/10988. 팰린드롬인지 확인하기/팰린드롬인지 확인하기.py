word = input()

# 슬라이싱을 이용해서 단어 역순과 비교
if word == word[::-1]: # 문자 값 비교는 '==' 사용
    print(1)
else:
    print(0)