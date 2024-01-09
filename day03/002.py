#str int float bool

#literal
#3
#3.14
#"3"
#"3"
#'"3"', "'3'" #'',""을 자체적으로 쓸수있음
#"""3"""      #들여쓰기가능

#함수 : 기능에 이름이 붙어있다. 왜? 재사용하려고
#함수가 동작하려면 내가 원하는 값을 넘겨줘야한다 -> 인자
print(3,4,5,sep = '')
#인자중에 이름이 정해진 인자(sep = 값 : 빈칸을 값으로 채움)


#다음과 같이 출력하시오
#신씨가 소리질렀다. "도둑이야".

print('신씨가 소리질렀다. "도둑이야".')
#print()함수를 통해 출력하시오
# naver;kakao;sk;samsung
# naver/kakao/sk/samsung

print("naver","kakao","sk","samsung",sep = ";")
print("naver","kakao","sk","samsung",sep = "/", end = '33')
#sep의 기본은 공백이지만 바꿀 수 있다.
#end의 기본은 줄바꿈이지만 바꿀 수 있다.


