# S: 숭실대, K: 고려대, H: 한양대 참여도
S, K, H = map(int, input().split())

# 총합이 100 이상인 경우
if S + K + H >= 100:
    print("OK")
    
else:
    # 참여도가 가장 낮은 대학 출력
    if S == min(S, K, H):
        print("Soongsil")
    elif K == min(S, K, H):
        print("Korea")
    else:
        print("Hanyang")
