import sys

count = 0

for _ in sys.stdin:
    count += 1

print(count)


# sys.stdin

# 표준 입력 전체를 의미
# EOF가 나올 때까지 입력 스트림을 그대로 읽을 수 있음
# input()처럼 EOFError를 발생시키지 않음