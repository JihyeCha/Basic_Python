## 제 2장 연습문제1
# - 사용자한테 이름과 나이를 입력하게 한다. 사용자가 100살이 되는 년도를 화면에 출력하는 프로그램을 작성하라.

name = input("이름을 입력하시오: ")   # input()은 사용자의 입력을 받아 출력함.
age = input("나이를 입력하시오: ")
year = 2021 - age + 100   # 사용자가 100살이 되는 년도 = 현재 연도(2021) - 현재 사용자의 나이 + 100
print(name + "씨는 " + str(year) + "년에 100살이 되십니다.")   # 정수 변수는 str()을 적용하여 문자열로 변환할 수 있다.




## 제 2장 연습문제2
# - 사용자로부터 3개의 숫자를 받아서 평균을 계산하고 결과를 출력하는 프로그램을 작성하라.

n1 = int(input("첫 번째 숫자를 입력하시오: "))   # 사용자로부터 받은 문자열은 int() 함수를 적용하여 정수로 바꾼다.
n2 = int(input("두 번째 숫자를 입력하시오: "))
n3 = int(input("세 번째 숫자를 입력하시오: "))

average = (n1 + n2 + n3)/3   # 평균(average)은 자료 전체의 합을 자료의 수로 나눈 값이다.

print(n1, n2, n3, "의 평균은 ", average, "입니다.")




## 제 2장 연습문제3
# - 사용자로부터 원의 반지름을 입력받아서 원의 면적을 계산하는 프로그램을 작성해보자.

radius = int(input("반지름을 입력하시오: "))   # 반지름(radius), input()은 사용자의 입력을 받아 출력
area = 3.14 * radius * radius   # 원의 넓이는 3.14 x 반지름의 제곱 이다.   # 곱셈을 나타내는 기호는 *이다.
print("반지름이 ", radius, "인 원의 넓이는 ", area, "입니다.")




## 제 2장 연습문제4
# - 원의 반지름을 정수 radius에 저장한다.radius의 초기값은 50이다. radius변수를 20씩 증가하면서 (0,0), (100,0), (200,0) 좌표에 원을 3개 그려보자.
#   터틀그래픽을 이용하고 반복문은 사용하지 않는다.

import turtle   # 터틀 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언한다.
t.shape("turtle")   # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

radius = 50; t.up(); t.goto(0, 0); t.down(); t.circle(radius)   # 반지름 radius, 터틀그래픽에서 거북이가 이동할 때 선이 그려지지 않게 하려면 t.up()하여 펜을 들 수 있고, t.down()하여 펜을 내려놓을 수 있다.
radius = radius + 20; t.up(); t.goto(100, 0); t.down(); t.circle(radius)   # 위 반지름에 + 20을 하고, (100, 0)으로 이동 후 반지름이 70인 원을 그린다.
radius = radius + 20; t.up(); t.goto(200, 0); t.down(); t.circle(radius)   # 위 반지름에 + 20을 하고, (200, 0)으로 이동 후 반지름이 90인 원을 그린다.




## 제 2장 연습문제5
# - 삼각형의 한 변의 길이를 side 변수로 나타낸다. side 변수의 초기값은 100이다. side 변수를 이용하여 화면에 삼각형을 그려보자.

import turtle   # 터틀 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언한다.
t.shape("turtle")   # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

side = 100   # side 변수의 값은 100이다.
t.forward(side)   # side 변수 값만큼 앞으로 이동
t.left(120)   # 정삼각형은 외각이 120도를 이뤄야 내각 60도가 만들어진다.
t.forward(side)
t.left(120)
t.forward(side)




## 제 2장 연습문제6
# - 5번 문제에서 삼각형 한 변의 길이를 200으로 변경한다고 하자. 5번 코드에서 어디만 수정하면 되는가?

side = 200  으로만 수정하면 된다.




## 제 2장 연습문제7
# - 다음과 같은 그림을 그리는 프로그램을 작성하시오. 이때 작은 사각형의 한 변의 길이는 side 변수에 저장하고, 거북이가 회전하는 각도는 angle 변수에 저장한다.

import turtle   # 터틀 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언한다.
t.shape("turtle")   # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

side = 50   # side 변수의 값은 50이다,
angle = 90   # angle 변수의 값은 90이다.
t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side);   # side 변수 값만큼 앞으로 이동, angle 변수 값만큼 회전
t.right(angle); t.forward(side)   # 줄의 끝이어서 ;를 안씀.
t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side);
t.right(angle); t.forward(100); t.right(180)   # 줄의 끝이어서 ;를 안씀.
t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side); 
t.right(angle); t.forward(side)   # 줄의 끝이어서 ;를 안씀.
t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side);


