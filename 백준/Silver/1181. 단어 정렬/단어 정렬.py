# 단어의 개수
N = int(input())

words = []
sorted_words = []

for _ in range(N):
    word = input()
    words.append(word)    
    
# 중복 제거 후 정렬:
# 1. 단어 길이 기준 오름차순 -> len(word)
# 2. 길이가 같으면 사전 순으로 정렬 -> word
sorted_words = sorted(set(words), key = lambda word : (len(word), word))

for word in sorted_words:
    print(word)
    
    
# lambda 함수
# lambda 매개변수: 표현식

# 이름 없는 함수(익명 함수)
# 주로 정렬, map, filter 등의 key 인자에서 사용
# 항상 값을 반환하며, 간단한 계산을 한 줄로 표현할 때 적합함