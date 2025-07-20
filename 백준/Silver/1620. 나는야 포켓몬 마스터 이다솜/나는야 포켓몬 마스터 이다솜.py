# N: 도감에 수록된 포켓몬 수 (1부터 N번까지 번호 부여)
# M: 맞춰야 하는 문제 수
N, M = map(int, input().split())

# 이름 <-> 번호 양방향 조회를 위한 딕셔너리
name_idx = {}  # 이름 -> 번호
idx_name = {}  # 번호 -> 이름


# 포켓몬 이름을 딕셔너리에 저장
for i in range(1, N+1):
    name = input()
    name_idx[name] = i
    idx_name[i] = name

# 포켓몬 정보 출력
for _ in range(M):
    question = input()

    if question.isdigit():              # 숫자(번호) 입력 시
        print(idx_name[int(question)])  # -> 이름 출력
    else:                               # 문자(이름) 입력 시
        print(name_idx[question])       # -> 번호 출력


# isdigit()
# 문자열이 숫자로만 이루어졌는지 확인
# ex. '123' -> True, 'a12' -> False