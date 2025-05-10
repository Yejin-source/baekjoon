# 테스트 케이스의 개수
T = int(input())

# 1부터 T까지 T번 반복
for x in range(1, T+1):
    A, B = map(int, input().split())

    sum = A + B
    print("Case #", x, ": ", sum, sep="")  # 공백 없이 출력


# 실패한 풀이
# print("Case #", x, ":", sum)
# 쉼표 사용 시 자동으로 공백이 삽입되는 문제 발생


# 공백 없이 출력하는 법

# 1. f-string 사용
# f"문자열 {표현식} 문자열"
# ex. print(f"Case #{x}: {sum}")

# 2. 문자열(str)로 변환 후 + 연산자 사용
# ex. print("Case #" + str(x) + ":", sum)

# 3. sep 옵션 사용
# 쉼표로 구분된 항목 사이에 삽입할 문자 지정
# 기본값은 ' '(공백)