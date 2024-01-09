#월급을 입력받아 1년치 소득세와 그것을 제외한 연봉 실수령액 계산
#소득세 3.3%로 계산
salary = int(input("당신의 월급은 : "))
annual_salary = salary * 12
INCOME_TAX_RATE = 0.033
income_tax = annual_salary * INCOME_TAX_RATE
real_annual_salary = annual_salary - income_tax
print(f"당신의 소득세 : {income_tax}, 당신의 실수령액은 : {real_annual_salary}")
