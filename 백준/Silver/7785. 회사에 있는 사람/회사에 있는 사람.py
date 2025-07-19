# 출입 기록의 수
n = int(input())

log = set()

for _ in range(n):
    name, status = input().split()
    
    if status == 'enter':
        log.add(name)      # enter -> 집합에 추가
    else:
        log.discard(name)  # leave -> 집합에서 제거

# 현재 회사에 있는 사람 출력 (사전 순의 역순)
for name in sorted(log, reverse=True):
    print(name)
    
    
# set 메서드 비교
# discard(x): x가 없으면 무시 (안전)
# remove(x): x가 없으면 에러 (주의 필요)