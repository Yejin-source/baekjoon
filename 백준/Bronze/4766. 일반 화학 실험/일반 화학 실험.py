temps = []

while True:
    temp = float(input())  # 소수로 입력 받기

    if temp == 999:  # 리스트 저장 X
        break

    temps.append(temp)

# 현재 온도와 이전 온도와의 차이 출력
for i in range(1, len(temps)):
    print(f"{temps[i] - temps[i-1]:.2f}")