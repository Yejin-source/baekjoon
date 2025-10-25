T = int(input())  # 입력 데이터 수

for _ in range(T):
    nums = list(map(int, input().split()))
    even_nums = [n for n in nums if n % 2 == 0]

    # 짝수 합과 최솟값 출력
    print(sum(even_nums), min(even_nums))