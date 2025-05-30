# 상의 N벌, 하의 N벌
N = int(input())

# 상의 선택: N가지
# 하의 선택: N-1가지 (상의와 다른 색만 가능)
result = N * (N-1)  # 전체 조합

print(result)