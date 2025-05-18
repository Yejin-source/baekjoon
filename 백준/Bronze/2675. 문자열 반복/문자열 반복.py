# 테스트 케이스의 개수
T = int(input())

# T번 반복
for _ in range(T):
    # R: 반복 횟수, S: 문자열
    R, S = input().split()  # 공백 기준으로 R과 S 분리
    R = int(R)              # 반복 횟수(R) 정수 변환


    # 문자열 S의 각 문자 반복
    for ch in S:
        print(ch * R, end='')  # 각 문자 ch를 R번 반복해서 출력
    print()  # 줄바꿈