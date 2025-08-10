name = input()
N = int(input())  # 후보 팀 수

best_team = ''
best_win_rate = -1  # 최대 우승 확률 (범위: 0~99 -> 첫 비교 시 갱신되도록 -1로 초기화)

for _ in range(N):
    team = input()
    full_name = name + team

    # 합친 이름에서 L, O, V, E 개수 세기
    L = full_name.count('L')
    O = full_name.count('O')
    V = full_name.count('V')
    E = full_name.count('E')

    # 우승 확률 계산 (주어진 공식)
    win_rate = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100

    # 최대 확률 갱신 (동률이면 사전순으로 앞서는 팀 선택)
    if win_rate > best_win_rate or (win_rate == best_win_rate and team < best_team):
        best_win_rate = win_rate
        best_team = team

print(best_team)