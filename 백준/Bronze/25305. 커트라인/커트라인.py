# N: 응시자의 수, k: 상을 받는 사람의 수
N, k = map(int, input().split())

# 학생들의 점수를 리스트로 저장 
x = list(map(int, input().split()))

# 점수를 내림차순으로 정렬 (sorted + reversed)
rev_x = list(reversed(sorted(x)))

# k번째로 높은 점수 출력
print(rev_x[k-1])


# 더 간단한 풀이
# x.sort(reverse=True)  # 리스트 자체를 내림차순 정렬
# sort()는 reversed()와 같이 사용할 수 없음