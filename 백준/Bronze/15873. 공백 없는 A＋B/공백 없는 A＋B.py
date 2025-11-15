num = input()

if len(num) == 2:      # 2자리 (A+B)
    A = int(num[0])
    B = int(num[1])

elif len(num) == 3:    # 3자리
    if num[1] == '0':  # (10+B)
        A = int(num[:2])
        B = int(num[2])
    else:              # (A+10)
        A = int(num[0])
        B = int(num[1:])

else:                  # 4자리 (10+10)
    A = int(num[:2])
    B = int(num[2:])

print(A+B)