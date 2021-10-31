## 제 4장 연습문제1
# - 왜 다음과 같은 수식이 오류를 발생시키는가? 올바르게 수정하라.
#   '나는 ' + 12 + '개의 사과를 먹었다.'

'나는 ' + str(12) + '개의 사과를 먹었다.'   # 문자열과 숫자는 합칠 수 없다. 숫자열을 문자열로 변환한 후에 문자열과 합쳐야 한다. 정수 변수는 str()을 적용하여 문자열로 변환 가능.




## 제 4장 연습문제2
# - 다음과 같은 수식을 계산하면 결과는 무엇인가?
#   'apple' + 'grape'
#   'apple' + 3

applegrape   # (문자열+문자열)하면 두 개의 문자열이 합쳐진다.
appleappleapple   # (문자열+n)하면 문자열이 반복된다.




## 제 4장 연습문제3
# - 다음과 같이 사용자가 입력한 문자열 중에서 처음 2글자와 마지막 2글자를 추출한 후에 이들을 합쳐서 출력해보자.
#   문자열을 입력하시오: python
#   pyon

str = input("문자열을 입력하시오: ")   # 문자열(string), input()은 사용자의 입력을 받아 출력한다.
print(str[0:2] + str[-2:])   # 처음 2글자는 s[0:2]로 추출할 수 있다. 마지막 2글자는 s[-2:]으로 추출이 가능하다.





## 제 4장 연습문제4
# - 다음과 같이 사용자가 입력한 문자열 뒤에 항상 "하는 중"을 붙이는 프로그램을 작성해보자.
#   문자열을 입력하시오: 청소
#   청소하는 중

s = input("문자열을 입력하시오: ")   # input()은 사용자의 입력을 받아 출력한다.
print(s + "하는 중")




## 제 4장 연습문제5
# - 사용자가 입력한 기호 안에 문자열을 삽입하려면 어떻게 해야 하는가? 기호는 문자 2개로 이루어져있다고 가정한다.
#   기호를 입력하시오: []
#   중간에 삽입할 문자열을 입력하시오: python
#   [python]

symbol = input("기호를 입력하시오: ")   # 기호(symbol), input()은 사용자의 입력을 받아 출력한다.
str = input("중간에 삽입할 문자열을 입력하시오: ")   # 문자열(string)
print(symbol[:1] + str + symbol[-1:])# 처음 1글자는 [0:1]로 추출할 수 있다. 마지막 1글자는 [-1:]으로 추출이 가능하다.





## 제 4장 연습문제6
# - 4개의 숫자가 들어 있는 리스트가 있다. 리스트 안의 숫자들을 꺼내서 합계를 계산하여 출력하는 프로그램을 작성하라.
#   반복문은 사용하지 않는다. 리스트의 길이는 항상 4라고 가정한다.
#   리스트 = [1, 2, 3, 4]
#   리스트 숫자들의 합 = 10

nlist = [1, 2, 3, 4]   # 정수(n)으로 구성된 리스트(list): nlist
sum = nlist[0] + nlist[1] + nlist[2] + nlist[3]   # 합(sum), 컴퓨터는 순서가 0123이라 [0],[1],[2],[3]으로 나타냄.
print("리스트 = ", nlist)
print("리스트 숫자들의 합 = ", sum)




## 제 4장 연습문제7
# - 사용자가 입력하는 3가지 색상을 리스트에 저장하였다가 하나씩 꺼내서 그 색상으로 채워진 원을 그리는 프로그램을 작성해보자.
#   반복문은 사용하지 않는다. 채워진 원을 그리려면 다음과 같은 문장을 사용한다.
#   t.fillcolor("yellow")   # 채워지는 색상을 지정한다.
#   t.begin_fill()   # 채우기를 시작한다.
#   t.circle(50)   # 채워진 원을 그린다.
#   t.end_fill()   # 채우기를 종료한다.
#   색상 #1을 입력하시오: yellow
#   색상 #2을 입력하시오: red
#   색상 #3을 입력하시오: blue

import turtle   # 터틀 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언한다.
t.shape("turtle")   # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

clist = []   # 색상(color) 리스트(list): clist
color = input("색상 #1을 입력하시오: ")   # input()은 사용자의 입력을 받아 출력한다.
clist.append(color)   # append는 주석
color = input("색상 #2을 입력하시오: ")
clist.append(color)
color = input("색상 #3을 입력하시오: ")
clist.append(color)

t.fillcolor(clist[0])   # 채워지는 색상을 clist의 첫 번째 색상으로 정한다.
t.begin_fill()   # 채우기를 시작한다.
t.circle(50)   # 채워진 원을 그린다.
t.end_fill()   # 채우기를 종료한다.

t.up()  # 펜을 든다.
t.goto(100, 0)   # (100, 0)으로 이동한다.
t.down()   # 펜을 내려 놓는다.
t.fillcolor(clist[1])   # 채워지는 색상을 clist의 두 번째 색상으로 정한다.
t.begin_fill()   # 채우기를 시작한다.
t.circle(50)   # 채워진 원을 그린다.
t.end_fill()   # 채우기를 종료한다.

t.up()   # 펜을 든다.
t.goto(200, 0)   # (200, 0)으로 이동한다.
t.down()   # 펜을 내려놓는다.
t.fillcolor(clist[2])   # 채워지는 색상을 clist의 세 번째 색상으로 정한다.
t.begin_fill()   # 채우기를 시작한다.
t.circle(50)   # 채워진 원을 그린다.
t.end_fill()   # 채우기를 종료한다.




## 제 4장 연습문제8
# - 사용자가 입력하는 3개의 좌표(x, y)를 리스트에 저장한다. 이들 좌표를 꺼내서 거북이를 이동하는 프로그램을 작성해보자.
#   x1: 0
#   y1: 0
#   x2: 100
#   y2: 100
#   x3: 200
#   y3: 100

import turtle   # 터틀 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언한다.
t.shape("turtle")   # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

coordinate_list = []   # 좌표(coordinate), 리스트(list)
list.append(int(input("x1: ")))   # append는 주석, int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다. x1의 값을 입력.
list.append(int(input("y1: ")))   # y1의 값 입력
list.append(int(input("x2: ")))   # x2의 값 입력
list.append(int(input("y2: ")))   # y2의 값 입력
list.append(int(input("x3: ")))   # x3의 값 입력
list.append(int(input("y3: ")))   # y3의 값 입력
t.goto(list[0], list[1])   # t.goto(list[0], list[1])과 같이 호출한다.
t.goto(list[2], list[3])
t.goto(list[4], list[5])

