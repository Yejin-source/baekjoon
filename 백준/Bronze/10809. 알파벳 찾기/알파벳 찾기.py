# 문자열을 리스트로 변환
S = list(input())

atoz = 'abcdefghijklmnopqrstuvwxyz'

# a 부터 z까지 반복
for ch in atoz:  
    
    # ch가 S에 있다면
    if ch in S:
        # 처음 등장하는 위치 출력
        print(S.index(ch), end=" ")
        
    # ch가 S에 없다면    
    else:
        # -1 출력
        print(-1, end=" ")


# index() 함수
# 리스트.index(값)
# 리스트에 처음 등장하는 위치(인덱스) 반환


# 다른 풀이
# S = input() # 리스트 변환 X

# a 부터 z까지 반복
# for ch in 'abcdefghijklmnopqrstuvwxyz':
#    print(S.find(ch), end=" ")


# find() 함수
# 문자열.find(찾을_문자)
# 문자열에서 찾을 문자가 처음 등장하는 위치 반환
# 존재하지 않을 경우 -1 반환