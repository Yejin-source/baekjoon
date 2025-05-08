n1, n2, n3 = map(int, input().split())

# 같은 눈이 3개 나온 경우
if n1 == n2 == n3:
    prize = 10000 + n1 * 1000
    
# 같은 눈이 2개 나온 경우    
elif n1 == n2:
    prize = 1000 + n1 * 100
elif n2 == n3:
    prize = 1000 + n2 * 100
elif n3 == n1:
    prize = 1000 + n3 * 100  
    
# 모두 다른 눈이 나온 경우    
else:
    prize = max(n1, n2, n3) * 100
  
print(prize)