# 숫자를 입력받아 CR(합계, 평균)UD
# 메뉴를 띄운다(1:숫자추가, 2:숫자출력, 999:종료)
numbers=[]
while True:
    print('==========   메  뉴   선  택   ===========')
    print('1.추가   2.합계  3.평균  4.삭제  999.종료')
    select=input('번호 입력 > ')
    if select=='999':
        print('종료합니다')
        break
    elif select=='1':
        num=int(input('추가할 숫자 : '))
        numbers.append(num)
    elif select=='2':
        print("합계 : ",sum(numbers))
    elif select=='3':
        print("평균 : ",sum(numbers)/len(numbers))
    elif select=='4':
        val=int(input('삭제할 값 : '))
        if val in numbers:
            numbers.remove(val)
        else:
            print('존재하지 않는 값입니다')
    print()    