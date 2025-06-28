# N번째 '666'이 포함된 숫자 찾기
N = int(input())

num = 666  # 검사 시작 숫자 
count = 0  # '666'이 포함된 숫자의 개수

while True:
    if '666' in str(num):  # '666'이 포함되어 있는 경우
        count += 1
        
        # 찾은 개수가 N과 같으면 출력 후 종료
        if count == N:
            print(num)
            break
        
    # 다음 숫자 확인
    num += 1