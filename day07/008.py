# 정수 2개를 인자로 받아 더해서 출력하는 함수 정의, 호출
def hap(a:int|float,b:int|float):
    print(a+b)

def hap2(a:int|float,b:int|float):
    return a+b

hap(1,2)
print(hap2(3,4))
result = hap2(3,4)
print(result)