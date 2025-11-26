N = int(input())  # 닉네임 수

for _ in range(N):
    nickname = input().split()
    nickname[0] = 'god'
    
    print(''.join(nickname))  # 공백 없이 출력