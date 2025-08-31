A, B, C = map(int, input().split())  # 세 개의 수
sorted_nums = sorted([A, B, C])      # 오름차순 정렬

sequence = input()  # 출력 순서

# 알파벳(순서)에 따라 대응하는 값 출력
for ch in sequence:
    if ch == 'A':
        print(sorted_nums[0], end=' ')
    elif ch == 'B':
        print(sorted_nums[1], end=' ')
    elif ch == 'C':
        print(sorted_nums[2], end=' ')


# 다른 풀이 (딕셔너리 활용)

# index_map = {'A': 0, 'B': 1, 'C': 2}

# for ch in sequence:
#     print(sorted_nums[index_map[ch]], end=' ')