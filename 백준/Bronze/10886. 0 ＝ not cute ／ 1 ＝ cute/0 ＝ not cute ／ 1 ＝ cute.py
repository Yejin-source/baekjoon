# 설문조사 한 사람의 수
N = int(input())

# N개의 투표 (0 또는 1)
opinions = [int(input()) for _ in range(N)]

if sum(opinions) > N // 2:  # 1(찬성)이 과반수를 넘으면
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')