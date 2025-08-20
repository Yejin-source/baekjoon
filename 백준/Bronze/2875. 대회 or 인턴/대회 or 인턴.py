# N: 여학생 수, M: 남학생 수, K: 인턴 참여 인원
N, M, K = map(int, input().split())

max_teams = min(N//2, M)      # 최대 팀 수
remain = N + M - max_teams*3  # 남는 인원

final_teams = max_teams

if remain < K:                    # 인턴 인원 부족
    need = (K - remain + 2) // 3  # 줄여야 할 팀 수
    final_teams -= need

print(final_teams )