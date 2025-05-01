all_students = set(range(1, 31))

submitted = set()  # 빈 집합 만들기
for _ in range(28):  # 변수를 사용하지 않는 경우 _ 사용 가능
    num = int(input())
    submitted.add(num)  # 하나씩 집합에 추가하기
    
# 집합끼리 연산으로 비교 가능    
not_submitted = all_students - submitted

for i in sorted(not_submitted):  # sorted: 새로 정렬된 리스트 반환
    print(i)


# set
# 중복을 허용하지 않으며 순서가 없음

# 한 번에 set으로 만드는 경우
# nums = set(map(int, input().split()))

# 파이썬 네이밍 컨벤션
# snake_case: 소문자로 작성, 단어 사이에 _ 사용


# 다른 풀이 (list 사용)
# submitted = []  # 빈 리스트 준비

# for _ in range(28):
#    num = int(input())
#    submitted.append(num)  # 리스트 맨 뒤에 num 추가

# for i in range(1, 31):
#    if i not in submitted:  # not in: 포함되지 않은 것
#        print(i)