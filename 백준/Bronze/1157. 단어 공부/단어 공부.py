# 입력 받은 문자열을 대문자로 변환
word = input().upper() 

# 중복된 문자 제거 후 리스트로 변환
word_list = list(set(word))

# 알파벳의 사용 횟수를 저장할 리스트
cnt = []


# word_list의 문자별 사용 횟수를 cnt에 저장
for ch in word_list:
    cnt.append(word.count(ch))    

# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    # 가장 많이 사용된 알파벳 출력
    print(word_list[cnt.index(max(cnt))])
        
        
# set(집합)
# 자동으로 중복 제거
# 순서가 없기 때문에 인덱싱 불가 -> list로 변환하면 가능
# 대소문자 구분 ('a' ≠ 'A')