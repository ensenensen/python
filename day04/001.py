# #75 80 70 국어점수가 있을 때 표현해보자 -> 집합타입(sequence)
# #값 하나 저장 타입: int float str bool
# #값 여러개를 저장하는 타입 list, tuple, dictionary, set

# a = 75
# b = 80
# c = 70

# print(a)
# print(b)
# print(c)


# kor = [75,80,70]
# #kor의 타입을 출력하시오
# print(type(kor)) # list 출력됨

# print(kor[0])
# print(kor[1])
# print(kor[2])
# #집합을 만들기에 변수의 개수가 줄어들기에 관리가 편함

# #조건문, 반복문으로 처리
# #kor 리스트의 원소를 하나씩 꺼내서 item에 담는다.
# for item in kor:
#     print(item)

# #리스트는 변경가능 튜플은 변경 불가
# 과일 = ["사과","귤","수박"] #리스트
# 과일2 = ("사과","귤","수박") #튜플 (읽기전용)

# #Ceate Read Update Delete / cud가 변경이라는 영역에포함

# #리스트, 튜플 프린트하기
# for item in 과일:
#     print(item)

# for item in 과일2:
#     print(item)





# 리스트 [   ] : 인덱스를 가지고있다
a = [3,4,5]
# print(a[0])
# print(a[1])
# print(a[2])
print(a)


# 리스트에 값 추가 => append
# 리스트이름.append(값) -> 리스트 마지막에 값 추가
a.append(6)
print(a)

# 지정위치에 값 추가 => insert
# 리스트이름.insert(위치,값) ->지정위치에 값 추가
a.insert(1,10)
print(a)

# for : 범위 내 반복
# for 변수이름 in 범위 :
#       실행문
# for 원소 in a :
#     print(원소)