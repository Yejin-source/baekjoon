num = input()  # 9자리 이하의 수
count = 0      # 단계 수

while len(num) > 1:
    prod = 1  # 각 자릿수의 곱 저장
    
    # 각 자릿수 곱하기
    for n in num:
        prod *= int(n)
        
    num = str(prod)
    count += 1

print(count)