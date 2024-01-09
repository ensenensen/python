# kor = 75, eng = 80
# 평균이 70 이상이면 합격, 아니면 불합격
kor = 75
eng = 80
avg = (kor+eng)/2

if avg >= 70 :
    print('합격')
else :
    print('불합격')

# 210초 -> 3분 30초
time = 210
minute = time//60
second = time%60
print(f'{minute}분 {second}초')

# 분과 초를 입력하면 초를 출력
# 5분 10초 -> 310초
minute = int(input("분 : "))
second = int(input("초 : "))
time = 60*minute+second
print(time,'초')

# 일수 입력받아 몇개월 몇일 출력
# 333일 -> 11개월 3일
days = int(input("일 : "))
month = days//30
day = days%30
print(f'{month}개월 {day}일')