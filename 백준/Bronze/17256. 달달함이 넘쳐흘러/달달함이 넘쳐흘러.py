ax, ay, az = map(int, input().split())  # A의 x, y, z
cx, cy, cz = map(int, input().split())  # C의 x, y, z

# B 좌표 계산
bx = cx - az
by = cy // ay
bz = cz - ax

# B의 x, y, z 출력
print(bx, by, bz)