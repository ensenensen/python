#초를 입력하면 몇분 몇초인지 출력

#second = int(input("원하는 초 : "))
#num1 = second // 60
#num2 = second % 60
#print(f"{num1}분 {num2}초 입니다.")

#분, 초 입력하면 초를 출력
#코드상에 값이 직접 나타나는것 : literal

minute = int(input("원하는 분 : "))
second = int(input("원하는 초 : ")) 
#상수를 표현하기위해 대문자로 표현
SECONDS_PER_MINUTE = 60                 
result = minute * SECONDS_PER_MINUTE + second
print(f"몇초 인가? : {result}초")

