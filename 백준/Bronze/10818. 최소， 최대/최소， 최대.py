# N개의 정수
N = int(input())
# 배열 입력
arr = list(map(int, input().split())) # 리스트로 변환 후 저장

print(min(arr), max(arr))