scores = list(map(int, input().split()))
max_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]

# zip: 점수와 최대 점수를 같은 위치끼리 묶어서 비교
for s, ms in zip(scores, max_scores): 
    if s > ms:
        print('hacker')
        break
else:
    if sum(scores) >= 100:
        print('draw')
    else:
        print('none')