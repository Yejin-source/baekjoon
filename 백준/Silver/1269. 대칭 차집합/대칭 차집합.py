# A: 집합 A의 원소 개수, B: 집합 B의 원소 개수
A, B = map(int, input().split())

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

only_A = set_A - set_B  # 집합 A에만 존재
only_B = set_B - set_A  # 집합 B에만 존재

# 대칭 차집합: (A-B)와 (B-A)의 합집합
sym_diff = only_A | only_B

print(len(sym_diff))


# 대칭 차집합 (A ^ B)
# sym_diff = set_A ^ set_B