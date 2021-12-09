## 제 6장 연습문제1
# 2부터 100 사이의 모든 짝수를 출력하는 반복 루프를 작성한다.

for i in range(1, 101):   # for 변수 in range()는 반복문에 사용된다.   # range에 횟수를 지정하면 숫자가 0부터 시작하지만, 시작하는 숫자와 끝나는 숫자를 지정해서 반복할 수 있음.
    if (i%2==0):   # x%2한 결과가 0이면 x는 짝수이다.   # 만약 i%2한 결과(나머지)가 0이라면,
        print(i, end=" ")   # 변수 i와, 끝에 " "를 출력하라.





## 제 6장 연습문제2
# 어떤 사람이 복리이자율 7%로 1000만원을 저금했을 경우에 2000만원이 되는데 몇년이 걸리는지 계산하기 위하여 다음과 같은 코드를 작성하였다. 잘못된 점은 없는지 체크해보자.
# year = 0
# balance = 1000
#
# while balance >= 2000 : 
#    year = year + 1
#    interest = balance * 0.07
#    balance = balance + interest
# print(year, "년이 걸립니다.")

while balance >= 2000 을 while balance <= 2000 으로 바꿔야 한다. # while문은 반복문의 일종이고, 특정한 조건이 참일 경우 계속해서 명령문들이 반복해서 실행된다. 조건이 거짓이 되는 순간 그만한다. 
# 'while balance >= 2000'은 'balance가 2000보다 크거나 같다면'인데, balance 값이 1000이므로 2000보다 클 수 없다. 즉, 조건이 거짓이 되어 반복문이 실행되지 않는다. 그러므로 'while balance <= 2000'으로 바꿔야 한다.





## 제 6장 연습문제3
# 다음 코드의 출력을 예상해보자. 각 단계에서 변수의 값을 예상해보시오.
# n = 1234                                                #(1)처음 n값: 1234,    # (2)처음 n값: 123,    #(3)처음 n값: 12,    #(4) 처음 n값: 1
# sum = 0
# while n > 0 :
#    difit = n % 10    # %는 나머지를 계산하는 연산자이다.   # (1)나머지: 4,   # (2)나머지: 3,    # (3)나머지: 2,   # (4)나머지: 1
#    sum = sum + digit                                    # (1)sum값: 4,    # (2)sum값: 3,    #(3)sum값: 2,     # (4)sum값: 1 
#    n = n // 10    # //은 나눗셈에서 몫을 계산한다.        # (1)n값: 123,    # (2)n값: 12,    #(3)n값: 1,    # (4)n값: 0
# print(sum)

digit = n % 10
sum = sum + digit
n = n // 10
맨 위의 n 값은 1234, 123, 12, 1 순으로 작아지고, sum 과 나머지도 4, 3, 2, 1 순으로 작아진다. 마지막의 n 값 또한 123, 12, 1, 0순으로 작아진다. n 이 0이 되고, 반복이 끝나면서 sum 값이 출력된다. sum 값은 n 이 0이 될 때까지 10으로 나누었을 때의 나머지(digit)를 모두 더한 값이다.
출력되는 sum 값은 나머지들의 합인 4+3+2+1 = 10 이다.





## 제 6장 연습문제4
# 사용자에게 곱셈 퀴즈를 내고 답을 사용자로부터 받는 프로그램에서 사용자가 올바른 답을 입력할 때까지 반복하도록 수정하여 보자.

import random    # 랜덤 모듈을 불러온다.

x = random.randint(1, 10)   # randint(a,b)함수는 a이상, b이하의 범위에서 임의의 정수를 골라 돌려준다.
y = random.randint(1, 10)

correct = x * y   # 정답(correct answer)에서 correct만 씀, *는 곱하기
while True:    # 어떤 조건이 만족될 때까지 반복하는 것은 while 루프이다.   
    user = int(input("%s * %s 는 "%(x, y)))    # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다.   # %s를 쓰고 ""를 벗어나서 %변수를 써주면 그 값이 출력된다. 변수 2개를 쓰려면 "%s %s" %(변수, 변수) 형식이다.
    if(user == correct):   # 만약 사용자가 입력한 값과 정답(correct)이 같다면,
        print("정답입니다.")   # 이를 출력하라.
        break;    # 결과가 True이면 break 문을 실행하여 루프를 빠져나온다.
    else:   # 이 외의 값이라면
        print("틀렸습니다. 다시 입력해주세요.")  # 이를 출력하라.




        
## 제 6장 연습문제5
# 사용자가 입력한 정수의 합을 계산하는 프로그램을 작성하자. 사용자가 0을 입력하기 전까지 정수를 계속하여 읽도록 한다.

print("입력하시는 정수의 합을 계산합니다. 0을 입력하시면 종료됩니다.")
sum = 0
while True:    # 무한 루프를 작성하고 사용자가 입력한 값이 0이면 break 문장을 실행하여 반복 루프를 빠져나간다. 무한 루프는 while True:로 만든다.   
    user = int(input("정수를 입력하세요.: "))    # 사용자에게 정수를 입력받는다.   # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다.
    if user == 0 :   # 만약 사용자가 입력한 정수가 0이라면,
        print("합은 ",sum,"입니다.")    # 이를 출력하라.
        break;    # 결과가 True이면 break 문을 실행하여 루프를 빠져나온다.
    else:    # 이 외의 값이라면
        sum = sum + user   # 0과 사용자가 입력한 정수들을 더하라.





## 제 6장 연습문제6
# 난수 생성 함수를 사용해서 2개의 주사위를 던졌을 때 나오는 수를 다음과 같이 출력하여 보자.

import random    # 랜덤모듈을 불러온다.

for i in range(2):   # for 변수 in range()는 ()안에 입력한 횟수만큼 반복해준다.
    r1 = random.randint(1, 6)    # 첫번째 주사위   # 1부터 6 사이의 난수를 발생하려면 r = random.radint(1, 6) 문장을 사용한다. 프로그램의 첫 부분에 import random 문장도 추가해야 한다.
    r2 = random.randint(1, 6)    # 두번째 주사위
    print("첫번째 주사위 = %s 두번째 주사위 = %s" %(r1, r2))   # %s는 위의 변수(r1과 r2)와 동일.   # %s를 쓰고 ""를 벗어나서 %변수를 써주면 그 값이 출력된다. 변수 2개를 쓰려면 "%s %s" %(변수, 변수) 형식이다.

    



## 제 6장 연습문제7
# 터틀그래픽과 반복을 사용하여 눈 모양을 그려보자.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

for i in range(6):    # for 변수 in range()는 ()안에 입력한 횟수만큼 반복해준다.
    t.forward(100); t.forward(-30); t.left(60); t.forward(30); t.forward(-30); t.right(120); t.forward(30); t.forward(-30); t.left(60); t.forward(-70); t.left(60);   # 파이썬에서 문장 뒤에 ; 기호를 붙이면 한 줄에 여러 개의 문장을 쓸 수 있다.   # forward()는 앞으로 ()픽셀만큼 이동, left()나 right()는 ()각도만큼 회전.





## 제 6장 연습문제8
# 우리는 이번 장에서 터틀 그래픽으로 별을 그려보았다. 이 코드를 응용하여서 다음과 같이 10개의 별을 그리는 프로그램을 작성하라. 별들은 시작 각도가 약간 다르다.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

for i in range(10):   # for 변수 in range()는 ()안에 입력한 횟수만큼 반복해준다.
    for s in range(5):   # s(star)    # 별을 그리는 코드를 반복한다. 
        t.left(144)   # 왼쪽으로 144도 회전(별의 꼭지점은 72도를 두 번 회전해서 144도)
        t.forward(100)   # 앞으로 100픽셀 이동
    t.left(10)   # 왼쪽으로 10도 회전    # 하나의 별을 그리는 반복이 끝나면 left(10)을 실행한다.





## 제 6장 연습문제9
# 반복과 난수를 함께 사용하면 화면에 랜덤한 원을 그릴 수 있다. 화면에 10개의 랜덤한 원을 그리는 프로그램을 작성하라. 원의 중심과 반지름이 모두 난수이어야 한다.

import turtle    # 터틀 모듈을 불러온다.
import random    # 랜덤 모듈을 불러온다.
t=turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

for i in range(10):   # for 변수 in range()는 ()안에 입력한 횟수만큼 반복해준다.
    x = random.randint(-100,100)    # x좌표, -100부터 100사이의 난수를 발생
    y = random.randint(-100,100)    # y좌표, -100부터 100사이의 난수를 발생
    r = random.randint(1,100)    # 반지름(radius)    # 1부터 100 사이의 난수를 발생하려면 r = random.randint(1, 100) 문장을 사용한다. 프로그램의 첫 부분에 import random 문장도 추가해야 한다.
    t.up()    
    t.goto(x,y)    # (x,y)로 이동
    t.down()    
    t.circle(r)    # 반지름이 r인 원을 그린다.





## 제 6장 연습문제10
# 다음과 같이 거북이를 왕복 달리기시키는 프로그램을 작성해보자.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

for i in range(5):     # for 변수 in range()는 ()안에 입력한 횟수만큼 반복해줌.
    t.forward(100)    # 앞으로 100픽셀 이동
    t.right(90)    # 오른쪽으로 90도 회전
    t.forward(10)    # 앞으로 10픽셀 이동
    t.right(90)    # 오른쪽으로 100픽셀 이동
    t.forward(100)   # 앞으로 100픽셀 이동
    t.left(90)    # 왼쪽으로 90도 회전
    t.forward(10)    # 앞으로 10픽셀 이동
    t.left(90)    # 왼쪽으로 90도 회전





## 제 6장 연습문제11
# 다음의 터틀 그래픽 프로그램을 분석해보자. 학습하지 않은 함수가 있다면 인터넷에서 조사하여 보자.
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.color('red', 'yellow')
# t.begin_fill()
# while True:
#    t.forward(200)
#    t.left(170)
#    if abs(t.pos()) < 1:
#       break
# t.end_fill()

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.
t.color('red', 'yellow')    # color(c1, c2) 함수는 도형의 선 색상과 채우기 색상을 c1과 c2로 설정한다.
t.begin_fill()    # begin_fill()를 호출하면 속이 채워진 도형이 그려진다.
while True:
   t.forward(200)
   t.left(170)
   if abs(t.pos()) < 1:    # pos()함수는 거북이의 좌표를 반환한다. abs()는 절댓값을 계산한다.   # 거북이 위치좌표의 절댓값이 1보다 작을 때, 반복 루프를 멈춘디.
      break     # break는 반복 루프를 빠져나오는 명령어이다.
t.end_fill()    # 채우기를 끝내라.





## 제 6장 연습문제12
# 터틀 그래픽과 반복을 사용하여 싸인(sine) 그래프를 그려보자. 거북이를 싸인값에 따라서 움직이면 된다.

import math   # 싸인값은 sin() 함수로 계산이 가능하다. 프로그램의 첫 부분에 import math를 추가한다.
import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

for x in range(360):
    t.goto(x, 100*math.sin(3.14*x / 180.0))    # 각도를 라디안으로 변환해야 한다. radian = 3.14 * degree / 180.0 수식을 사용한다.
