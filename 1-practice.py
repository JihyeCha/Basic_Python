## 제 1장 - 연습문제1
# - "환영합니다.", "파이썬의 세계에 오신 것을 환영합니다.", "파이썬은 강력합니다"를
#   화면에 출력하는 프로그램을 작성하시오.

print("환영합니다.")   # print("")는 "" 안의 내용을 그대로 출력한다.
print("파이썬의 세계에 오신 것을 환영합니다.")
print("파이썬은 강력합니다")




## 제 1장 - 연습문제2
# - 다음 프로그램의 실행 결과를 쓰시오.
#   print("반갑습니다. 파이썬!")
#   print(2*3/10)
#   print("Hello", "World", "!!!")

반갑습니다. 파이썬!   # 출력 결과에는 print("")는 나오지 않는다.
0.6   # print()안에 ""가 없으면 계산 결과가 출력된다. *는 곱하기, /는 나누기이다.
Hello World !!!   # print("")안의 내용이 그대로 출력된다.




## 제 1장 - 연습문제3
# - 파이썬 쉘을 사용하여 한 주가 몇 시간에 해당하는지를 계산해보자.

# 한 주는 7일, 하루는 24시간이므로 7*24를 한다.

168




## 제 1장- 연습문제4
# - 터틀 그래픽에서 거북이를 이동시켜서 다음과 같은 그림을 그려보자. forward(), left(),right()함수만을 사용한다.

import turtle   # turtle 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언한다.
t.shape("turtle");   # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

t.forward(100)   # 앞으로 100팍셀 이동
t.left(90)   # 왼쪽으로 회전
t.forward(100)   # 앞으로 100픽셀 이동
t.right(90)   # 오른쪽으로 이동
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)




## 제 1장 - 연습문제5
# - 터틀 그래픽에서 width() 함수를 호출하면 거북이가 그리는 선의 두께를 두껍게 한다.
#   거북이를 이동하여서 다음과 같이 두께가 10인 선을 그려보자.

import turtle   # turtle 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언.
t.shape("turtle")   # turtle 모듈의 아이콘을 거북이 모양으로 선언.
t.width(10)   # 선 두께 width를 10으로 선언.
t.forward(100)
t.left(90)
t.forward(100)




## 제 1장 연습문제6
# - 터틀 그래픽에서 color() 함수를 호출하면 거북이가 그리는 선의 색상을 변경할 수 있다.
# - 색상을 파랑색으로 변경하여 다음과 같이 길이가 100픽셀인 선을 그려보자.

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")   # 선의 색상을 파란색으로 선언.
t.forward(100)




## 제 1장 연습문제7
# - 터틀그래픽에서는 거북이의 모양을 삼각형, 원, 사각형으로 변경할 수 있다. 다음과 같이 shape()함수를 사용하면 된다.
#   사각형으로 변경하고 100픽셀 길이의 직선을 그려보자.

import turtle
t = turtle.Turtle()
t.shape("square")   # turtle 모듈의 아이콘을 사각형으로 선언한다.
t.forward(100)




## 제 1장 연습문제8
# - 터틀그래픽에서 거북이가 이동할 때 선이 그려지지 않게 하려면 t.up()하여 펜을 들 수 있다. 반대로 t.down()은 펜을 내려놓는 명령어이다.
#   거북이를 화면 좌표 (100,200)으로 이동시키려면 t.goto(100,200)을 호출한다. 이들 명령어를 조합하여 다음과 같은 그림을 그려보자.


import turtle
t = turtle.Turtle()
t.shape("turtle")
t.up()   # 펜을 든다.
t.goto(0, 0)   # 터틀그래픽의 좌표는 수학 좌표계와 동일, 화면 중앙이 원점(0, 0)이 된다.,  # 원점으로 이동한다.
t.down()   # 펜을 내려놓는다.
t.forward(100)   # 100픽셀만큼 앞으로 이동한다.

t.up()   # 펜을 든다.
t.goto(0, 100)   # (0, 100)으로 이동한다.
t.down()   # 펜을 내려놓는다.
t.forward(100);   # 100픽셀만큼 앞으로 이동한다.,  # ;은 명령어를 끝낼 때 사용.





# 제 1장 연습문제 9 (오륜기)
# - 터틀그래픽에서 t.circle(100)이라고 입력하고 실행하면 화면에 반지름이 100인 원이 그려진다. 
#   이들 명령어를 조합하여서 화면에 오륜기를 그리는 프로그램을 작성해보자.

import turtle
t = turtle.Turtle()
t.shape("turtle");

t.up(); t.width(5); t.color("blue"); t.goto(-220, 0); t.down(); t.circle(100)   # 거북이가 이동할 때 선이 그려지지 않게 하려면 t.up()하여 펜을 들 수 있고, 펜을 내려놓을 땐 t.down()을 사용.
t.up(); t.width(5); t.color("black"); t.goto(0, 0); t.down(); t.circle(100)
t.up(); t.width(5); t.color("red"); t.goto(220, 0); t.down(); t.circle(100)
t.up(); t.width(5); t.color("yellow"); t.goto(-110, -100); t.down(); t.circle(100)
t.up(); t.width(5); t.color("green"); t.goto(110, -100); t.down(); t.circle(100)
t.write("종료하려면 화면클릭")

