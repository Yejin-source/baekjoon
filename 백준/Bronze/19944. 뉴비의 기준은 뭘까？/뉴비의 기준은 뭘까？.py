# N: 대회 참가 가능 학년, M: 참가자 학년
N, M = map(int, input().split())

if M <= 2:
    print("NEWBIE!")  # 1, 2학년
elif M <= N:
    print("OLDBIE!")  # 3학년 이상, N학년 이하
else:
    print("TLE!")    