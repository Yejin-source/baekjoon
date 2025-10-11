T = int(input())  # 테스트 케이스 수

for _ in range(T):
    S = input()  # 문자열 (알파벳 대문자)

    total = 0
    for i in range(65, 91):  # A(65)~Z(90)까지의 아스키 코드 합
        total += i

    # 문자열 아스키 코드 합
    used = sum(ord(ch) for ch in set(S))  # ord(): 문자 -> 아스키 코드 변환

    # 등장하지 않는 문자열의 아스키 코드 합
    print(total - used)