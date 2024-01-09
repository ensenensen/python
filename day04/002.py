a = '345'
b = int(a) # 345
c = float(a) #345.0
d = str(b) #"345"

ar = [3,4,5]
# ar을 튜플로 변환해 저장
br = tuple(ar)
print(type(br))

#리스트에 원소를 추가한다 : append
#java개념으로는  .은 멤버연산자이다 / list 가 클래스로서 정의되어있기에
#append는 프리랜서가 아니라 ar에 소속된 함수 -> method
ar.append(100)
ar.insert(1,1000) #지정하는 위치에 지정하는값넣기
print(ar)

xr = (10,20,30)
#xr에 40을 추가한 다음 출력
xr2 = list(xr)
xr2.append(40)
xr = tuple(xr2) #실무작업에서는 이런경우 돌려놔야한다.
print(xr)
