onboard = 0  # 현재 탑승 인원
peak = 0     # 최대 탑승 인원

for _ in range(4):
    get_off, get_on = map(int, input().split())
    onboard += get_on - get_off  # 현재 인원 갱신
    peak = max(peak, onboard)    # 최대 인원 갱신

print(peak)