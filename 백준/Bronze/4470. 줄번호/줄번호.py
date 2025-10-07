N = int(input())  # 줄의 개수

for i in range(1, N+1):
    sentence = input()
    
    # f-string 사용: "번호. 내용" 형식으로 출력
    print(f"{i}. {sentence}")