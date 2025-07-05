# 문자열로 수 입력받기
N = input()

# 자릿수를 내림차순 정렬
sorted_N = sorted(N, reverse=True)

# 하나의 문자열로 결합 후 출력
print(''.join(sorted_N))


# join()
# '구분자'.join(문자열 리스트) 

# 숫자 리스트는 join 불가능
# -> 숫자 리스트를 문자열로 합칠 때는 map() 사용
# ex) ''.join(map(str, [1, 2, 3])) -> '123'