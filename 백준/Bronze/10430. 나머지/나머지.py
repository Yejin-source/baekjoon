A, B, C = map(int, input().split())

print((A + B) % C)  # 전체 합을 나눈 결과
print(((A % C) + (B % C)) % C)  # 나머지끼리 더해서 다시 나눈 결과

print(((A * B) % C))  # 전체 곱을 나눈 결과
print(((A % C) * (B % C)) % C)  # 나머지끼리 곱해서 다시 나눈 결과