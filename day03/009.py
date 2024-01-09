# 국어, 영어 점수 입력받아 합계와 평균을 출력
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))

sum = kor + eng
avg = sum / 2

#f-string
print(f"합계:{sum}점, 평균:{avg}점")

