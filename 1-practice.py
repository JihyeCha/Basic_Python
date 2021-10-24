# 1장 - 추가 연습 문제 (오륜기)
# - 터틀그래픽에서 t.circle(100)이라고 입력하고 실행하면 화면에 반지름이 100인 원이 그려진다. 
#   이들 명령어를 조합하여서 화면에 오륜기를 그리는 프로그램을 작성해보자.

import turtle
t = turtle.Turtle()
t.shape("turtle");  
t.up(); t.width(5); t.color("blue"); t.goto(-220, 0); t.down(); t.circle(100)  # width는 너비, color는 색깔, goto는 좌표
t.up(); t.width(5); t.color("black"); t.goto(0, 0); t.down(); t.circle(100)
t.up(); t.width(5); t.color("red"); t.goto(220, 0); t.down(); t.circle(100)
t.up(); t.width(5); t.color("yellow"); t.goto(-110, -100); t.down(); t.circle(100)
t.up(); t.width(5); t.color("green"); t.goto(110, -100); t.down(); t.circle(100)
t.write("종료하려면 화면클릭")
