#숫자를 2개 입력받아 다음과 같이 출력하시오
#예) 3과 8의 합은 11, 곱은 24입니다.

num1 = int(input("첫번째 수"))
num2 = int(input("두번째 수"))

print(f"{num1}과 {num2}의 합은 {num1 + num2}, 곱은 {num1 * num2}입니다.")

a = 23
b = (a%7 * 7 / a%7)
result = a + b
print(result)