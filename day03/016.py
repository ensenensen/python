#숫자로 입력을 받아서 음수면 양수로 양수면 음수로변환

#number = int(input("숫자 : "))

#if number < 0:
 #   number = -number

#print(f"결과 : {number}")

#길이를 입력받아 센치 <-> 인치로 변경
#1인치 = 2.54cm
length = int(input("길이 : "))
kind = input("종류[센치, 인치] : ")

if kind == "센치":
    length = (((length / 2.54) * 100) // 1) / 100
    print(f"{length}인치로 변경완료")
elif kind == "인치":
    length = (((length * 2.54) * 100) // 1) / 100
    print(f"{length}센치로 변경완료")
else:
    print("형식에 맞게 작성해주세요")




