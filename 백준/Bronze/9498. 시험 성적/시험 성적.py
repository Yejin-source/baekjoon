# 점수를 입력받은 후 정수형으로 변환
score = int(input())

if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')
    
# elif -> else if 축약
# 하나의 숫자를 입력받는 경우 map() 사용 X

# ex. 90을 입력받으면 map(int, "90") -> [9, 5]
# 각 문자 하나씩을 숫자로 바꾸기 때문에 잘못된 방식