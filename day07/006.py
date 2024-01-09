import e005
from e005 import hello,python

e005.hello()
hello()

e005.python()
python()

def message():
    print("A")
    print("B")

# 함수는 동시에 실행되지 않는다(한번에 하나씩 실행)
# 병렬 프로그래밍 : 함수를 동시에 실행하는 것
message()
print("C")
message()