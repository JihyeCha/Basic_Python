## 제 7장 연습문제1
# 눈사람을 그리는 함수를 작성하고 이 함수를 여러 번 호출하여서 랜덤한 위치에 눈사람을 그리는 프로그램을 작성하라. 아래 실행 결과와 최대한 비슷하게 작성해보자.

def draw_snowman(x, y):    # 눈사람을 그리는 함수
    
#눈사람 윗부분
    t.up()    # 펜을 든다.
    t.goto(x, y+110)    # (x, y+110) 좌표로 이동한다.
    t.down()    # 펜을 내려놓는다.
    
    t.begin_fill()    # 채우기를 시작한다.
    t.circle(35)    # 반지름이 35인 채워진 원을 그린다.
    t.end_fill()    # 채우기를 종료한다.
    
#눈사람 중간부분
    t.up()    # 펜을 든다.
    t.goto(x, y+80)    # (x, y+80) 좌표로 이동한다.
    t.down()    # 펜을 내려놓는다.

    t.lt(20)    # 왼쪽(left)으로 20도 회전
    t.fd(90); t.fd(-90)     # 앞(forward)으로 90픽셀 이동, -90픽셀 이동(-이므로 뒤로 이동)
    t.lt(115)    # 왼쪽으로 115도 회전
    t.fd(90); t.fd(-90)    # 앞으로 90픽셀 이동, -90픽셀 이동
    t.seth(0)    # seth() 를 이용하면 360도 중 원하는 각도로 거북이의 머리 방향을 바꿀 수 있음.  0도로 머리 방향을 바꿈.

    t.begin_fill()    # 채우기를 시작한다.
    t.circle(25)    # 반지름이 25인 채워진 원을 그린다.
    t.end_fill()    # 채우기를 종료한다.

#눈사람 아랫부분
    t.up()    # 펜을 든다.
    t.goto(x, y)    # (x, y)좌표로 이동한다.
    t.down()    # 펜을 내려놓는다.

    t.begin_fill()    # 채우기를 시작한다.
    t.circle(50)    # 반지름이 50인 채워진 원을 그린다.
    t.end_fill()    # 채우기를 종료한다.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.
s = turtle.Screen(); s.bgcolor('skyblue');    # 터틀 그래픽에서 배경을 하늘색으로 만들려면 이 문장을 실행한다.

t.color('black', 'white')    # 펜 색을 검은색(black)으로, 채우기 색을 흰색(white)로 지정.

for i in range(3):    # for 변수 in range()는 ()안의 수 만큼 반복해준다. 3번 반복.
    draw_snowman(200*i-50,0)    
    




## 제 7장 연습문제2
# 6각형을 그리는 draw_hexa() 함수를 작성하고 이 함수를 호출하여서 다음과 같은 벌집 모양을 화면에 그려보자.

# 6각형을 그리면 forward(100)과 left(60)을 6번 되풀이하면 된다.


import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.
t.speed(0)    # turtle 모듈의 속도를 0으로 설정.

def hexagon():    # 6각형(hexagon) 함수
    for i in range(6):   # for 변수 in range()는 ()안의 수 만큼 반복해준다. 6번 반복
        t.fd(100)    # 앞(forward)으로 100픽셀 이동
        t.lt(360/6)    # 왼쪽(left)으로 60도 회전
        
for i in range(6):   # for 변수 in range()는 ()안의 수 만큼 반복해준다. 6번 반복
    t.fd(100)    # 앞(forward)으로 100픽셀 이동
    t.rt(60)    # 왼쪽(left)으로 60도 회전





## 제 7장 연습문제3
# 함수 f(x) = x^2 + 1을 계산하는 함수를 작성하고 이 함수를 이용하여 f(x)를 그려보자.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.
t.speed(0)    # turtle 모듈의 속도를 0으로 설정.

def f(x):    # f(x) 함수로 정의
    return x**2+1    # x**2 + 1 값을 반환

t.goto(200, 0)    # (200, 0)좌표로 이동한다.
t.goto(0, 0)    # (0,0)좌표로 이동한다.
t.goto(0, 200)    # (0,200)좌표로 이동한다.
t.goto(0, 0)    # (0,0)좌표로 이동한다.

for x in range(150):     # for 변수 in range()는 ()안의 수 만큼 반복해준다. x를 0에서 150까지 반복
    t.goto(x, int(0.01*f(x)))    # (x, int(0.01*f(x)))좌표로 이동한다. # int()는 문자열을 숫자로 바꾼다. 함수의 값이 무척 커질 수 있으므로 함수의 값에 0.01을 곱한다.





## 제 7장 연습문제4
# 터틀 그래픽에서 거북이를 움직이지 않고 선을 긋는 함수 draw_line()을 정의하고 이것을 이용하여 다음과 같은 거미줄과 같은 모양을 그려보자. 거북이는 항상 중앙에 위치한다.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.
t.speed(0)    # turtle 모듈의 속도를 0으로 설정.

def draw_line():    # 선을 그리는 함수
    t.forward(100)    # 앞으로 100픽셀 이동.
    t.backward(100)    # 뒤로 100픽셀 이동
    
for x in range(12):    # for 변수 in range()는 ()안의 수 만큼 반복해준다. 12번 반복한다.
    t.right(30)    # 오른쪽으로 30도 회전
    draw_line()    # 선을 그리는 함수 반복





## 제 7장 연습문제5
# 다음과 같이 이름을 받아서 생일 축하 노래를 출력하는 함수 happyBirthday()를 작성하고 테스트하시오.

def happyBirthday(name):    # 생일 축하 노래를 출력하는 함수, 매개 변수 name을 통하여 이름을 받는다.
     print("Happy Birthday to you!")    # 이를 출력하라.
     print("Happy Birthday to you!")    # 이를 출력하라.
     print("Happy Birthday, dear " + name)    # 이를 출력하라.
     print("Happy Birthday to you!")    # 이를 출력하라.
     
happyBirthday("홍길동")





## 제 7장 연습문제6
# 사용자로부터 2개의 정수를 받아서 수학 문제를 만들어서 화면에 출력하는 함수를 작성하고 테스트하시오.

def sumProblem(x, y):    # 더하기 문제(sum 합, problem 문제)
    sum = x + y    # 변수 sum은 x + y
    sentence = "정수" + str(x) + "+" + str(y) + "의 합은?"    # 문장(sentence), # 문자열과 숫자는 합칠 수 없다. 숫자열을 문자열로 변환하고 문자열과 합쳐야 함. 정수 변수는 str()을 적용하여 문자열로 변환가능하다.
    print(sentence)    # sentence를 출력하라.
     
def main():    # 메인 함수
    a = int(input("첫 번째 정수: "))    # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다.
    b = int(input("두 번째 정수: "))    # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다.
    sumProblem(a, b)    # 더하기문제(a, b)
    
main()    # main()을 다시 호출





## 제 7장 연습문제7
# 파이를 나타내는 PI=3.14를 전역 변수로 하여 원의 면적을 계산하는 함수 circleArea(radius)과 원의 둘레를 계산하는 함수 circleCircumference(radius)를 작성하고 테스트하라.

PI = 3.14159265358979    # 파이

def circleArea(radius):     # 원의 면적을 계산하는 함수
    return PI*radius*radius    # PI*반지름*반지름 값을 반환.

def circleCircumference(radius):    # 원의 둘레를 계산하는 함수
    return 2*PI*radius    # 2*PI*반지름 값을 반환.

def main():    # 메인 함수
    print("반지름이 5인 원의 면적: ", circleArea(5))     # 이를 출력하라.
    print("반지름이 5인 원의 둘레: ", circleCircumference(5))    # 이를 출력하라.

main()    # main()을 다시 호출.





## 제 7장 연습문제8
# 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 함수를 각각 작성하고 테스트하라.

def add(a, b):    # 더하기(add) 함수
    print("(%d + %d)" % (a, b), end=" ")    # 이를 출력하라. # d는 정수(digit)이다.
    return a + b    # a + b 값을 반환.

def subtract(a, b):    # 빼기(subtract) 함수 
    print("(%d - %d)" % (a, b), end=" ")    # 이를 출력하라.
    return a - b     # a-b 값을 반환.

def multiply(a, b):    # 곱하기(multiply) 함수
    print("(%d * %d)" % (a, b), end=" ")    # 이를 출력하라.
    return a * b    # a*b 값을 반환.

def divide(a, b):     # 나누기(divide) 함수
    print("(%d / %d)" % (a, b), end=" ")    # 이를 출력하라.
    return a / b    # a / b 값을 반환.

what = add(20, 10)    # 변수 what은 더하기(20, 10)
print(" = ", what)    # 이를 출력하라.

