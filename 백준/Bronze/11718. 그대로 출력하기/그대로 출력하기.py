# try-except문 사용_예외(에러) 처리
try:
    while True:  # 무한 루프
        text = input()
        print(text)
except EOFError:
    pass  # 에러를 무시하고 넘어가기


# EOF (End Of File)
# 입력의 끝

# EOFError
# input()이 더 이상 읽을 게 없는 경우
# 즉 EOF를 만나는 경우 발생하는 에러

# pass
# 아무것도 하지 않고 지나가는 것
# 실행할 코드가 아직 존재하지 않거나 필요 없는 경우 자리를 채워줌
# 빈 블록은 에러가 나기 때문에 pass로 채우는 것

# pass를 사용하는 경우
# 1. 비어 있는 함수, 클래스를 만들 때
# 2. 조건문에서 아무 것도 하지 않을 때
# 3. 예외(에러) 처리를 무시할 때