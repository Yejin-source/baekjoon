while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
    
    
# try-except (≒ 자바 try-catch) 
# try:
    # 오류가 발생할 수 있는 구문    
# except Exception as e:
    # 오류가 발생할 경우 실행
# else:
    # 오류가 발생하지 않을 경우 실행
# finally:    
    # 무조건 마지막에 실행

   
# 실패한 방법    
# while True:
#    A, B = map(int, input().split()) # 한 번 더 실행돼서 실패
#    if(A is None and B is None):
#        break
#    else:
#        print(A+B)

# null값 확인
# is None