# 파일의 개수
N = int(input())

file_sizes = list(map(int, input().split()))
cluster_size = int(input())

total = 0  # 사용한 디스크 공간

for file in file_sizes:
    if file == 0:  # 파일 크기가 0인 경우
        continue
    
    # 해당 파일이 차지하는 클러스터 개수 (올림 나눗셈)
    clusters = (file + cluster_size - 1) // cluster_size
    
    # 클러스터 개수 × 클러스터 크기
    total += clusters * cluster_size

print(total)