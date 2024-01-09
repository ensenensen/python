#1년은 몇초인가
#DAYS_PER_YEAR = 365
#HOURS_PER_DAY = 24
#MINUTES_PER_HOUR = 60
#SECONDS_PER_MINUTE = 60
#print(f"{DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE}초")
#
#45분간 일하고 10분씩 휴식. 전체 근무시간 480이면 
#휴식시간의 합계는?
#
#all_worktime = 480
#result = all_worktime // 55
#print(result * 10)


#숫자를 입력받아 1의 자리까지 버리고 출력
#예) 3512 -> 3510

#num = int(input("숫자 : "))
#reslut = (num // 10) * 10
#print(reslut)

#자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수

#number = int(input("숫자 : "))
#result = number // 7 
#result2 = result * 7
#print(result2)

#자연수를 입력받아 그 숫자보다 작은 최대의 7의 배수
# 17 -> 14 21 -> 14
number = int(input("숫자 : "))
result = (number-1) // 7
result2 = result * 7  
print(result2)

