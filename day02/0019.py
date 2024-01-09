#kor에 75, eng에 80
#평균이 70이상이면 합격 아니면 불합격
kor, eng = 7, 80
avg = (kor + eng) / 2

print(f"당신의 평균점수 : {avg}")
if avg >= 70:
    print("너 합격.")
else:
    print("너 불합격.")

print("수고하셨습니다.")

