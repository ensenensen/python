#몇일 인지 입력받아 몇개월 며칠인지 출력
#333 = 11개월 3일

days = int(input("며칠이냐?"))
DAYS_PER_MONTH = 30
month = days // DAYS_PER_MONTH
left_days = days % DAYS_PER_MONTH
print(f"총 계산 : {month}개월 {left_days}일")

