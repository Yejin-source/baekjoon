N = int(input())

# 전체 점의 개수: (한 변의 점 개수)^2 = (2^N + 1)^2
dot = (2 ** N + 1) ** 2  # ** : 거듭제곱
print(dot)


# 한 변의 점 개수 변화    
#  0     1     2     3      4       5
# 2x2 → 3x3 → 5x5 → 9x9 → 17x17 → 33x33

# 한 변의 점 개수: 2^N + 1 → 전체 점 개수: (2^N + 1)^2