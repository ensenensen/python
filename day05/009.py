a = [1,2,3,4,5]

while True:
    print('==============')
    print("1. 값 추가")
    print("2. 리스트 출력")
    print('3. 합계')
    print('4. 평균')
    print("999. 종료")
    print('==============')
    select = input('번호 선택 > ')
    if select == '1':
        num = int(input('추가할 값 =) '))
        a.append(num)
        print(num,'이(가) 추가되었습니다')
    elif select == '2':
        print(a)
    elif select == '3':
        print("합계 : ",sum(a))
    elif select == '4':
        print("평균 : ",sum(a)/len(a))
    elif select=='999':
        print('감사합니다')
        break
    else :
        print('다시 입력해주세요')
    print('')