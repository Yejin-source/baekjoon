words = []   # 다섯 줄 문자열 리스트
result = ''  # 세로로 읽은 글자 누적 변수


for i in range(5):
    words.append(input())  # 입력값을 한 줄씩 리스트에 추가 

# 열 기준으로 반복 (문자열은 최대 15글자)
for j in range(15):
    # 각 행을 반복
    for k in range(5):
        # 현재 행에 j번째 글자가 존재하는 경우만 처리
        if len(words[k]) <= j:
            continue  # 글자가 없는 경우 건너뜀
        else:
            result = result + words[k][j]  # 세로 방향으로 글자 추가
    
print(result)