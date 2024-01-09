x = 15.82
print(x//1.0)

a,b = 19,5
# %연산 금지. 나머지 4를 출력하시오(+,-,*,/,//)
print(a-(b*(a//b)))

# y를 1의 자리에서 버림 : 450
y = 453
result = y - y%10
print(result)

result2 = (y//10)*10
print(result2)

# 숫자를 입력하면 그 숫자보다 작은 최대의 짝수
# 7 -> 6
num1 = int(input("숫자 입력 : "))
a = num1//2*2
print(a)

import math
# 숫자를 입력하면 가장 가까운 7의 배수 출력
# 15 -> 21
num2 = int(input("숫자 입력 : "))
b = math.ceil(num2/7)*7
print(b)