#숫자를 입력받아 3의 배수인지 아닌지 출력하시오

number = int(input("원하는 숫자 : "))
if number % 3 == 0:
    print(f"{number}는 3의 배수입니다.")
else:
    print(f"{number}는 3의 배수아님")


#점수를 입력받아 90점 이상 우수 70점이상 패스 미만이면 낙제라고 출력
    
jumsu = int(input("원하는 숫자 : "))
if jumsu >= 90:
    print("우수")
elif jumsu >= 70:
    print("패쓰")
else:
    print("낙제")


