N = int(input())

# 첫째 줄부터 N번째 줄까지 별 출력
for i in range(1, N+1):
    spaces = (N - i) * " " # 공백 부분
    stars = i * "*"        # 별 부분
    print(spaces + stars)  # 합쳐서 출력