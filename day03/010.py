#집의 가로와 세로를 입력받아 너비를 평으로 출력
#3.3 제곱미터가 1평 

horizontal = int(input("집의 가로 : ")) 
verticla = int(input("집의 세로 : ")) 

result1 = horizontal * verticla
result2 = (((result1 / 3.3) * 100) // 1) / 100 # 간략화를 위해 소수 2번째 밑은 짜름

print(f"평 수 계산 값 : {result2}")


