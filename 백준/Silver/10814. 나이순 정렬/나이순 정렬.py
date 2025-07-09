# 온라인 저지 회원의 수
N = int(input())

people = []

for _ in range(N):
    age, name = input().split()
    people.append((int(age), name))  # (나이, 이름) 형태로 저장
      
# 나이 기준 오름차순 정렬 (stable sort)
sorted_people = sorted(people, key = lambda person: person[0])

for age, name in sorted_people:
    print(age, name)
    

# stable sort
# 정렬 기준이 동일한 요소들의 "원래 순서"를 유지하는 정렬 방식