# 세 문자열
s1 = input()
s2 = input()
s3 = input()

# 세 문자열의 첫 글자 집합
firsts = {s1[0], s2[0], s3[0]}

if firsts == {'l', 'k', 'p'}:  # l, k, p로 시작할 경우
    print("GLOBAL")
else:
    print("PONIX")