#연산
#산술연산(총 6개)
# + - * /
#몫: //, 나머지:%

#print(18 / 5)
#print(18 // 5)
#print(17 % 5)


#x = 16.30202
#x의 소수점 이하를 버리고 출력하시오

#print(int(x))
#print(x // 1)

#a = 19
#b = 6
#%연산 금지, 나머지를 출력하시오
#num1 = (a / b) - (a//b) 
#num2 = a - (b *num1) #실제로 나눠지는양
#result = a - num2 #나머지

#print(result)

#y = 453231321
#y를 1의 자리에서 버림 
#result = y // 10
#result2 = result * 10
#print(result2)


#숫자를 입력하면 그 숫자보다 작은 최대의 
#7 -> 6

#숫자를 입력하면 가장 가까운 7의 배수를 출력
#15 -> 21, 21 -> 21 이런느낌

# a = int(input("원하는 숫자 : "))
# c = int(input("원하는 배수 : "))
# b = ((a +((c- a%c)%c))// c) #무조건 더 많은 7의배수, if의 역할
# result = b * c 
# print(result)





a = 3.14
print(int(a)) # 3.14




num = 354
# 일의 자리 숫자만 버림하고 출력
print(num-(num%10))
# 354 - 4 = 350