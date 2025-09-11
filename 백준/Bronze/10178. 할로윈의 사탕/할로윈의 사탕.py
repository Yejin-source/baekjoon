# 테스트 케이스 수
T = int(input())

for _ in range(T):
    # c: 사탕 개수, v: 형제 수
    c, v = map(int, input().split())

    print('You get', c//v, 'piece(s) and your dad gets', c%v, 'piece(s).')


# 다른 풀이 (f-string)

# print(f'You get {c//v} piece(s) and your dad gets {c%v} piece(s).')