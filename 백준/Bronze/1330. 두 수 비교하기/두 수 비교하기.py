# map() 함수를 사용해서 자료형 변환
A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
    
# elif -> else if 축약