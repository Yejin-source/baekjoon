P = int(input())  # 동아리 학생 수 

sw = 0     # 소프트웨어개발과
embed = 0  # 임베디드소프트웨어개발과
ai = 0     # 인공지능소프트웨어개발과
fresh = 0  # 1학년 (소속 과 X)

for _ in range(P):
    G, C, N = map(int, input().split())   # 학년, 반, 번호

    if G == 1:
        fresh += 1
    else:
        if C == 1 or C == 2:
            sw += 1
        elif C == 3:
            embed += 1
        else: 
            ai += 1

print(sw)
print(embed)
print(ai)
print(fresh)