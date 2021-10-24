## 제 2장 - 도전문제 2
# - 거북이가 앞으로 움직이는 거리도 변수 x에 저장해보자. 변수의 값을 변경하면서 위의 프로그램을 실행해보자.

import turtle
t = turtle.Turtle()
t.shape("turtle")
radius = 50   # 변수 radius와 그 값을 선언
x = 30   # 변수 x와 그 값을 선언
t.circle(radius)   # 반지름이 50픽셀인 원이 그려진다.
t.forward(x)   # forward는 fd로 쓸 수도 있다. 같은 명령어이다. 앞으로 30픽셀 이동한다.
t.circle(radius)   # 반지름이 50픽셀인 원이 그려진다.
x = 50
t.fd(x)   # 앞으로 50픽셀 이동한다.
t.circle(radius)   # 반지름이 50픽셀인 원이 그려진다.
