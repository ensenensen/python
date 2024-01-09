#주민번호를 입력받아 
#1900년대면 1,2 2000년이면 3,4
#태어난 년도를 계산해 나이를 출력

jumin = input("주민번호 : ")
this_year = 2024
print(jumin[7])
if jumin[7] == '1' or  jumin[7] == '2': # in ('1','2') 도 됨
    result1 = int('19' + jumin[0:2])
    result2 = (this_year - result1) + 1
    print(f"당신의 나이 : {result2}")
elif jumin[7] == '3' or  jumin[7] == '4':
    result1 = int('20' + jumin[0:2])
    result2 = (this_year - result1) + 1
    print(f"당신의 나이 : {result2}")

