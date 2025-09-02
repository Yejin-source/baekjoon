# A: 구간의 시작, B: 구간의 끝
A, B = map(int, input().split())

seq = []
i = 1

# 수열 길이가 B보다 작을 동안 반복
while len(seq) < B:
    seq.extend([i] * i)  # extend: 원소들을 풀어서 추가
    i += 1

print(sum(seq[A-1:B]))