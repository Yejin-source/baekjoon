# 수직선 위에 있는 좌표의 수
N = int(input())

# 좌표 리스트 입력
xs = list(map(int, input().split()))

# 중복 제거 후 오름차순 정렬
sorted_xs = sorted(set(xs))

# 좌표값을 인덱스로 압축한 딕셔너리 생성
compress = {num: idx for idx, num in enumerate(sorted_xs)}

# 각 좌표의 압축값 출력 (인덱스)
for x in xs:
    print(compress[x], end=' ')


# 딕셔너리 컴프리헨션
# {key: value for 변수 in 반복가능한 객체}

# enumerate() 함수
# 반복 가능한 객체에 자동으로 인덱스 부여
# (index, value) 형태의 튜플 반환


# 시간 초과(TLE) 발생한 코드 _ list.index() 반복 사용

# N = int(input())
# xs = list(map(int, input().split()))

# sorted_xs = sorted(set(xs))

# for i in xs:
#     print(sorted_xs.index(i), end=' ')