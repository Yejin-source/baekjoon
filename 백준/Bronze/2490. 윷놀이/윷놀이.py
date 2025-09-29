# 0의 개수에 따라 매핑 (도:A, 개:B, 걸:C, 윷:D, 모:E)
result = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E'}

for _ in range(3):
    yut = list(map(int, input().split()))
    
    zeros = yut.count(0)  # 0 개수 세기
    print(result[zeros])  # 개수에 해당하는 알파벳 출력