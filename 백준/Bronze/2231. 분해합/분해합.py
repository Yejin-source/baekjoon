N = int(input())

# 1부터 N-1까지 검사
for i in range(1, N):
    # i의 분해합 = i + 각 자릿수의 합
    total = i + sum(map(int, str(i)))

    # 분해합이 N과 같다면 i는 생성자
    if total == N:
        print(i)
        break
else:
    # 생성자가 없는 경우
    print(0)