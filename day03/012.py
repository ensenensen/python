#반지름을 입력받아 원의 면적을 출력하시오(pi * r * r)
#                     둘레를 출력하시오(2 * pi * r)


#1.면적을 출력해야한다. 둘레를 출력해야한다.
#2.면적과 둘레가 있어야한다. 즉 면적과 둘레를 계산하고 출력기능도 있어야한다.
#3.계산은 면적 : pi * 반지름 * 반지름 | 출력은 어떻게하지? ->  print()로 출력하자
#4.계산은 둘리 : 2 * pi * 반지름
#5.반지름과 pi 는 어떻게 하는가
#6.반지름은 입력받으면 되고 pi는 원주율, 즉 상수이기에 3.14로 하자


num1 = int(input("반지름 : ")) #반지름
PI = 3.14
num2 = num1 * num1 * PI #면적
num3 = 2 * PI * num1 #둘레

print(f"원의 면적{num2} 원의둘레{num3}")
