# N: 듣도 못한 사람의 수, M: 보도 못한 사람의 수
N, M = map(int, input().split())

unheard = set(input() for _ in range(N))
unseen = set(input() for _ in range(M))


# 두 목록에 모두 있는 사람들 (교집합)
common_names = unheard & unseen

print(len(common_names))

# 사전 순 정렬 후 출력
for name in sorted(common_names):
    print(name)