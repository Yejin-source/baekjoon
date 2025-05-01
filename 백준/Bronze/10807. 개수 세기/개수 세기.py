N = int(input())
A = list(map(int, input().split()))  # map 객체를 리스트로 변환
v = int(input())

print(A.count(v))  # 리스트.count(찾을 값)


# count 메서드
# 리스트에서 특정 값이 몇 번 나오는지 세어주는 함수