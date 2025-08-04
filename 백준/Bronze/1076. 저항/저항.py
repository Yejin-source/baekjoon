# 저항 색상별 숫자 딕셔너리
color = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

a = input()  # 첫 번째 자리 숫자
b = input()  # 두 번째 자리 숫자
c = input()  # 자릿수

# 저항 값 계산: 두 자리 수 × 10의 거듭제곱
value = (color[a] * 10 + color[b]) * (10 ** color[c])

print(value)