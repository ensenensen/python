numbers = [100,300,500,700]

# 위치 입력 del number[2]
# 값을 입력받아 위치 찾기
value = 500


index = 0
for num in numbers:
    if value==num:
        print(index)
        index = index+1