# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 정수 10개 리스트 변환
    A = list(map(int, input().split()))
    
    # 정렬 후 3번째 큰 값 출력
    print(sorted(A)[-3])