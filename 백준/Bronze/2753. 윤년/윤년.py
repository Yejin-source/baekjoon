year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(1)
else:
    print(0)

# and는 or보다 우선순위가 낮기 때문에
# or부터 계산되도록 괄호로 묶어주는 것이 좋음