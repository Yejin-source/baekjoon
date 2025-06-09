# A: 올라가는 거리, B: 미끄러지는 거리, V: 나무 막대 높이
A, B, V = map(int, input().split())

# (V-B): 마지막 날은 미끄러지지 않음
# (A-B): 하루에 올라가는 거리

if (V-B) % (A-B) == 0:  # 딱 맞게 도착하는 경우
    print((V-B) // (A-B))
else:
    print((V-B) // (A-B) + 1)  # 남는 거리가 있으면 하루 추가