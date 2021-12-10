## 6장 도전문제1
# 사용자로부터 정수 n을 받아서 n각형을 그리는 프로그램을 작성할 수 있는가?

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

s = turtle.textinput("","몇각형을 원하시나요?: ")    # textinput()함수는 문자열을 입력할 수 있는 입력창을 생성한다.
n = int(s)    # 사용자로부터 받은 문자열은 int() 함수를 적용하여 정수로 바꾼다.

for i in range(n):    # for 변수 in range()는 ()안에 입력한 횟수만큼 반복해준다. n번 반복.
    t.forward(100)    # 앞으로 100픽셀 이동
    t.left(360/n)    # 왼쪽으로 360/n 각도만큼 회전





## 6장 도전문제2
# 터틀 그래픽에서 거북이가 술에 취한 것처럼 랜덤하게 움직이게 해보자.

import turtle    # 터틀 모듈을 불러온다.
import random    # 랜덤 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

for i in range(30):    # for 변수 in range()는 ()안에 입력한 횟수만큼 반복해준다. 30번 반복.
    length = random.randint(1,100)    # 길이(length), 1과 100사이의 난수를 발생
    t.forward(length)    # 위의 값만큼 앞으로 이동
    angle = random.randint(-180,180)    # 각도(angle), -180과 180 사이의 난수를 발생
    t.right(angle)    # 오른쪽으로 angle 각도 만큼 회전

    
    
    

## 6장 도전문제3
# for 문을 이용하여서 팩토리얼을 계산해보자. 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다. 즉, n!=1×2×3×......×(n-1)×n이다.

n = int(input("정수를 입력하시오: "))    # 사용자로부터 받은 문자열은 int() 함수를 적용하여 정수로 바꾼다. input()은 사용자의 입력을 받아 출력한다.

fact = 1    # 팩토리얼(factorial, 여기선 fact까지만 나타냄) n!은 1부터 n까지의 정수를 모두 곱한 것.
for i in range(1, n+1):    # for 변수 in range(a,b)는 범위에 있는 숫자들을 반복 가능한 형태로 변환해주는 함수, a를 포함한 숫자보다 크고 b보다 작은(b 포함x)숫자를 반복함.
    fact = fact*i     # 팩토리얼 = 1 * 2×3×......×(n-1)×n
print(n, "!은 ",fact,"이다.")    # 이를 출력하라.




 
## 6장 도전문제4
# 반복문을 사용하여 별을 그려보자. 5번 반복하고, 반복할 때마다 거북이를 50픽셀만큼 전진시키고 오른쪽으로 144도 회전하면 별이 그려진다.

import turtle    # 터틀 모듈을 불러온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.
i = 0    # 변수 i의 값을 0으로 저장
while i < 5:   # while은 반복문, i가 5보다 작으면 반복.
    t.forward(50)    # 앞으로 50픽셀 이동 
    t.right(144)    # 오른쪽으로 144도 회전
    i = i + 1    # i의 값을 1씩 더해 5가 될 때까지 반복.
