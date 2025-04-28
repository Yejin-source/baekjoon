# while문 무한루프
while True:
    A, B = map(int, input().split())
    if(A == 0 and B == 0): # A와 B가 0일 때
        break              # 반복문 종료
    else:
        print(A+B)


# while문
# while 조건: