# 빈 리스트 생성
num_list = []

# 서로 다른 9개의 자연수 입력받기
for _ in range(9):
    num = int(input())
    num_list.append(num) # 리스트에 값 추가

# 최댓값
max_value = max(num_list)

print(max_value)
print(num_list.index(max_value)+1) # 최댓값 위치