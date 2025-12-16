A = int(input())  # X사 1리터당 요금
B = int(input())  # Y사 기본요금
C = int(input())  # Y사 기본요금이 되는 사용량 상한
D = int(input())  # Y사 1리터 당 추가요금
P = int(input())  # 한 달간 수도 양

x_cost = A * P

if P <= C:
    y_cost = B
else:
    y_cost = B + (P-C) * D

print(min(x_cost, y_cost))  # 더 저렴한 한 달 수도요금