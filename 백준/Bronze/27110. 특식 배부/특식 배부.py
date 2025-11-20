N = int(input())  # 치킨 마릿수
A, B, C = map(int, input().split())  # 각 종류를 선호하는 병사 수

# 가장 선호하는 치킨을 받을 수 있는 최대 인원수
print(min(N, A) + min(N, B) + min(N, C))