#숫자 2개 입력받아 큰수와 작은수 출력
#예 : 5 와 8중 큰수는 8 작은수는 5

num1 = int(input("1번 수"))
num2 = int(input("2번 수"))
max_number = max(num1, num2)
min_number = min(num1, num2)

print(f"가장 큰 수 {max_number} 가장 작은수 {min_number}")


