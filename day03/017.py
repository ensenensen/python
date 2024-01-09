#임의로 가정
#남자의 적정 체중은 키 - 100, 여자의 적정 체중은 키 - 105
#키를 입력받아 적정 체중을 출력하시오

height = int(input("당신의 키 : "))
gender = input("당신의 성별[남자,여자] : ")
if gender == "남자":
    body_weight = height - 100
    print(f"당신의 체중 : {body_weight}")
elif gender == "여자":
        body_weight = height - 105
        print(f"당신의 체중 : {body_weight}")
else:
      print("형식에 맞게 작성하시오")
