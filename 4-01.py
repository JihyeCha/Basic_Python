## 제 4장 자료의 종류 : 도전문제1
# - 사각형의 각 변에 "안녕하세요? 홍길동씨, 터틀 인사드립니다." 를 출력해보자.

import turtle
t = turtle.Turtle()
t.shape("turtle");

s = turtle.textinput("","이름을 입력하시오: ")

for i in range(4):   # range는 범위를 지정할 수 있는 자료형. 사각형인 경우의 범위(각 변)는 4이다.
    t.write("안녕하세요? " + s +"씨, 터틀 인사드립니다.")
    t.left(90)
    t.forward(100)
