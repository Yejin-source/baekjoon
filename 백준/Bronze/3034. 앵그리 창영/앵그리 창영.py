# N: 성냥 개수, W: 박스 가로 크기, H: 세로 크기
N, W, H = map(int, input().split())

# 박스 대각선 길이 (피타고라스)
diag = (W**2 + H**2) ** 0.5

for _ in range(N):
    match = int(input())  # 성냥 길이
    
    # 성냥이 대각선보다 짧거나 같으면 박스 안에 들어감
    if match <= diag:     
        print('DA')
    else:
        print('NE')


# 다른 풀이 (math.sqrt())

# import math 
# diag = math.sqrt(W**2 + H**2)  # 제곱근 반환