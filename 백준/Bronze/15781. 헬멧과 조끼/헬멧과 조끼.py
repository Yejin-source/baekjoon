# N: 헬멧 개수, M: 조끼 개수
N, M = map(int, input().split())

helmets = list(map(int, input().split()))
vests = list(map(int, input().split()))

print(max(helmets) + max(vests))  # 방어력 최댓값