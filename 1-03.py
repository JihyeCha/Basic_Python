## 제 1장 - 도전문제3
# -(1) 거북이를 움직여서 정삼각형을 그려보자. 회전하는 각도는 몇 도로 하여야 하는가?
# -(2) 거북이를 움직여서 정사각형을 그려보자. 회전하는 각도는 몇 도로 하여야 하는가?

# 터틀 모듈을 불러온다. -> import turtle
# 터틀을 t로 선언, import turtle as t 할 수 있음. -> t = turtle.Turtle()
# 터틀 모듈의 아이콘을 거북이 모양으로 선언 -> t.shape("turtle");
# ; 는 끝났다는 것임.
# 기본 아이콘은 classic, 삼각형은 triangle, 원은 circle 로
# 터틀 아이콘을 움직이려면 t.방향(각도)로 선언 -> ex) t.forward(100), t.left(90)등
# forward는 직진(이동 길이,  각 변의 길이)
# left or right는 회전(회전 각도, 정삼각형의 경우는 외각이 120도를 이뤄야 내각 60도가 만들어짐.

import turtle   # (1)
t = turtle.Turtle()
t.shape("turtle");
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

import turtle   # (2)
t = turtle.Turtle()
t.shape("turtle");
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

