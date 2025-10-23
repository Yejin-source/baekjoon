V = int(input())  # 심사위원 수

votes = input()  # 투표 결과

a = votes.count('A')  # A가 받은 표
b = votes.count('B')  # B가 받은 표

if a > b:
    print('A')
elif b > a:
    print('B')
else:  # 받은 표가 같은 경우
    print('Tie')