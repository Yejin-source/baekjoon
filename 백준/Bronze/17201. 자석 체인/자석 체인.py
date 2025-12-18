N = int(input())  # 자석 개수
a = input()       # 자석 연결 상태

for i in range(N-1):

    if a[2*i+1] == a[2*i+2]:  # 모두 연결된 상태
        print('No')
        break
else:
    print('Yes')