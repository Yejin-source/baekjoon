# 10진법 수 N을 B진법으로 출력
N, B = map(int, input().split())

# 진법 문자 목록
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''

# 진법 변환을 위해 반복
while N > 0:
    result = digits[N % B] + result  # 나머지를 문자로 변환해 앞에 추가
    N //= B                          # 몫으로 갱신해서 다음 자릿수 계산

print(result)