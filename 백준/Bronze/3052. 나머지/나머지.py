s = set() # 집합

# 10번 반복
for _ in range(10):
    num = int(input())
    rem = num % 42
    s.add(rem) # 나머지를 set에 추가 (중복 무시)

# 서로 다른 나머지 개수 출력
print(len(s))


# set(집합)              
# 자동으로 중복 제거
# 순서가 없음 -> 인덱싱 불가능
# 리스트와 정반대 (중복 허용, 순서 O)


# len(자료형)
# 자료형 안에 들어 있는 요소의 개수 반환