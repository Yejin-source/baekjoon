# 개선 코드: 반복문 사용해서 가독성 높임

payment = int(input())
change = 1000 - payment  # 거스름돈

coins = [500, 100, 50, 10, 5, 1]
count = 0

for c in coins:
    count += change // c  # 필요한 동전 개수 계산
    change %= c           # 남은 거스름돈 갱신

print(count)


# 이전 코드: 가독성 낮음

# print(change//500 + (change%500)//100 + (change%100)//50 + (change%50)//10 + (change%10)//5 + (change%5))
