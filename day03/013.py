#제어문 (control)
#순서를 바꾼다
#조건 : 결과가 이럴수도있고 저럴수도있다.
#반복

#홀짝 확인 
jumsu = 75
if jumsu % 2 == 0:
    print("짝수")
else:
    print("홀수")
    print("수고하셨습니다")

#점수가 90점 이상이면 우수, 70점이상 합격, 미만이면 재시험

jumsu = int(input("너의 점수 : "))
if jumsu >= 90:
    print("우수 합격")
elif jumsu >= 70: #여러개올수있음
    print("합격")
else:
    print("재시험")




