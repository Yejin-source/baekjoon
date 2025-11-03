# N, M: 관중석 크기(행, 열), K: 관중석 번호
N, M, K = map(int, input().split())

print(K // M, K % M)  # 자리 좌표 출력