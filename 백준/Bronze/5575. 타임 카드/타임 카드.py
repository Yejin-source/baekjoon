for _ in range(3):
    # 각 직원 출근/퇴근 시간
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    
    # 초 단위 변환
    t1 = h1*60*60 + m1*60 + s1
    t2 = h2*60*60 + m2*60 + s2
    
    t = t2 - t1  # 총 근무 시간 (초)
    
    h = t//60//60 % 24
    m = t//60 % 60
    s = t%60
    
    print(h, m, s)  # 각 직원 근무 시간