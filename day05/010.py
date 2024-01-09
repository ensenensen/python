list1 = [15,20,30,90]
# list1의 길이 -> len()

# a=0
# for x in list1:
#     a=a+1
# print(a)

# list1의 합계 출력
# aa = 0
# for x in list1:
#     aa=aa+x
# print(aa)

# list1의 평균(합계/개수) 출력
a = 0
aa = 0
for x in list1:
    a+=1
    aa+=x
print(aa/a)