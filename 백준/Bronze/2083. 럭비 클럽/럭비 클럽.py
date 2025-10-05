while True:
    name, age, weight = input().split()
    if name == '#' and age == weight == '0':  # 종료 조건
        break

    # 나이 > 17 또는 몸무게 >= 80 -> Senior, 그 외 -> Junior
    print(name, 'Senior' if int(age) > 17 or int(weight) >= 80 else 'Junior')