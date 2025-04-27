x = int(input())
y = int(input())

# 제 1사분면
if x > 0 and y > 0:
    print(1)
# 제 2사분면
elif x < 0 and y > 0:
    print(2)
# 제 3사분면
elif x < 0 and y < 0:
    print(3)
# 제 4사분면
elif x > 0 and y < 0:
    print(4)
    
# 논리 연산자 (자바랑 비교)
# and (&&)
# or (||)
# not (!)