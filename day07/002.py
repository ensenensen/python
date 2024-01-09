todos = [
    {"tno":1,"title":"자바","finish":False},
    {"tno":3,"title":"파이썬","finish":False}
]
tno=4
title = input('할일 입력 : ')
todo={"tno":tno, "title":title, "finish":False}
todos.append(todo)
tno=tno+1

# Read : for로 todos 출력
for todo in todos:
    print(todo)

# update : tno로 찾아 finish를 변경
input_tno=int(input('변경할 번호 : '))
for todo in todos:
    if todo['tno']==input_tno:
        todo['finish']=not todo['finish']
        break
    

print(todos)

# 번호를 입력받아 찾아서 출력
sno = int(input('검색할 번호 : '))
for todo in todos:
    if todo['tno']==sno:
        print(todo)
    else:
        print('존재하지 않습니다')
