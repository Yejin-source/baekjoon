while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == a2 == a3 == 0:  # 종료 조건
        break

    if a2 - a1 == a3 - a2:  # 등차수열(AP)
        print("AP", a3 + a2 - a1)
    else:                   # 등비수열(GP)
        print("GP", a3 * (a2 // a1))