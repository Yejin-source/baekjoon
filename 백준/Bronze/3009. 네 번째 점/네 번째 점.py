x_list = []
y_list = []

# 세 점의 좌표 입력
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)


# 한 번만 나온 x 좌표 값 찾기
for i in x_list:
    if x_list.count(i) == 1:
        x4 = i
        break  # 반복 중단

# 한 번만 나온 y 좌표 값 찾기
for i in y_list:
    if y_list.count(i) == 1:
        y4 = i
        break  # 반복 중단

# 네 번째 점의 좌표 출력
print(x4, y4)