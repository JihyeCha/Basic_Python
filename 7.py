## 제 7장 도전문제1
# n-각형을 그리는 함수를 작성해보자.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

def shape(length):    # 모양 함수, length는 한변의 길이
    s = turtle.textinput("", "몇각형을 원하시나요? : ")    # 텍스트 입력
    n = int(s)    # int()는 문자열을 숫자로 바꾼다.
 
    for i in range(n):    # for 변수 in range()는 ()안의 수 만큼 반복해준다.
        t.forward(length)     # length 값 만큼 앞으로 이동
        t.left(360/n)    # (360/n) 각도만큼 왼쪽으로 회전
        
t.up()    # 펜을 든다. 
t.goto(-200, 0)    # (-200, 0) 좌표로 이동한다. 
t.down()    # 펜을 내려놓는다. 
shape(100);    # shape() 함수를 호출한다.
    
t.up()    # 펜을 든다.
t.goto(0, 0)    # 원점(0, 0) 좌표로 이동한다.
t.down()    # 펜을 내려놓는다.
shape(100);    # shape() 함수를 호출한다.

t.up()    # 펜을 든다.
t.goto(200, 0)    # (200, 0) 좌표로 이동한다.
t.down()    # 펜을 내려놓는다.
shape(100);    # shape() 함수를 호출한다.





## 제 7장 도전문제2
# 한변의 길이와 색상을 지정하고, 도형 그리고 색을 채워보자.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

def square(length,index):    # 사각형(square)함수, length는 한변의 길이이다.
    t.color(colorList[index])    # 색상, 색상목록
    t.begin_fill()    # 채우기를 시작한다.
    for i in range(4):    # for 변수 in range()는 ()안의 수 만큼 반복해준다. 4번 반복.
        t.forward(length)    # length 값 만큼 앞으로 이동
        t.left(90)     # 왼쪽으로 90도 회전
    t.end_fill()    # 채우기를 끝낸다.

colorList = ["red", "blue", "green"]    # 색상목록: 빨간색, 파란색, 초록색
x = -200    # x는 -200

for i in range(len(colorList)):    # for 변수 in range()는 ()안의 수 만큼 반복해준다.
    t.up()    # 펜을 든다. 
    t.goto(x, 0)    # (-200, 0)좌표로 이동한다. 
    t.down()    # 펜을 내려놓는다. 
    square(100, i);    # square() 함수를 호출한다. 
    x+=200




