## 제 5장 연습문제1
# - 다음 프로그램의 출력은 무엇인가?
#   age = 20
#   if age < 20:
#      print('20살 미만')
#   else:
#      print('20살 이상')

20살 미만   # age < 20은 변수 age의 값이 20 미만인 경우에만 참이 된다.




## 제 5장 연습문제2
# - 1번 문제에서 age가 30이상이고 50이하인 것을 체크하려면 어떻게 해야하는가?

age = 20
if age >= 30 and age <= 50:   # 논리 연산자 and를 사용
    print('30살 이상 50살 이하')




## 제 5장 연습문제3
# - 사용자에게 현재 온도를 질문하고 온도가 25도 이상이면 반바지를 추천하고 25도 미만이면 긴바지를 추천하는 프로그램을 작성해보자.
#   현재 온도를 입력하시오: 10
#   긴바지를 입으세요

temp = int(input("현재 온도를 입력하시오: "))   # 온도(temperature), int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다. 시험 점수를 입력.
if temp >= 25:   # 만약 온도가 25도 이상히면 
    print("반바지를 입으세요.")   # 이를 출력하라.
else:   # 이 외의 경우라면
    print("긴바지를 입으세요.")   # 이를 출력하라.




## 제 5장 연습문제4
# - 학생의 시험 점수를 물어보고 시험 점수가 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 그 외의 점수라면 F학점을 주는 프로그램을 작성하라.

score = int(input("성적을 입력하시오: "))   # 점수(score), int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다. 시험 점수를 입력.

if score >= 90:   # if...elif...else 구문을 사용, 만약 점수가 90점 이상이라면
    print("A학점 입니다.")   # 이를 출력하라.
elif score >= 80:   # 만약 점수가 80점 이상이라면 
    print("B학점 입니다.")   # 이를 출력하라.
elif score >= 70:   # 만약 점수가 70점 이상이라면
    print("C학점 입니다.")   # 이를 출력하라.
elif score >= 60:   # 만약 점수가 60점 이상이라면
    print("D학점 입니다.")   # 이를 출력하라.
    
else :   # 이 외의 점수라면 
    print("F학점 입니다.")   # 이를 출력하라.




## 제 5장 연습문제5
# - 난수를 사용하여 1부터 100 사이의 숫자를 사용하는 뺄셈 문제를 생성하고 사용자에게 물어본 후에 사용자의 답변이 올바른지를 검사하는 프로그램을 작성하라.
#   28 - 9 = 19
#   맞았습니다.

import random   # 랜덤 모듈을 불러온다.
x = random.randint(1, 100)   # randint(a,b)함수는 a이상, b이하의 범위에서 임의의 정수를 골라 돌려준다.
y = random.randint(1, 100)
ans = int(input(str(x) + "-" + str(y) + "="))   # 답(answer), input()은 사용자의 입력을 받아 출력한다. 정수 변수는 str()을 사용하여 문자열로 변환 가능하다.
if ans == x - y :   # 만약 답이 x-y이면
    print("맞았습니다.")   # 이를 출력하라.
else :   # 이 외의 경우라면
    print("틀렸습니다.")   # 이를 출력하라.




## 제 5장 연습문제6
# - 사용자로부터 정수를 받아서 이 정수가 2와 3으로 나누어 떨어질 수 있는지를 출력하라.
#   정수를 입력하시오: 6
#   2와 3으로 나누어 떨어집니다.

n = int(input("정수를 입력하시오: "))   # 정수(n), input()은 사용자의 입력을 받아 출력한다.
if n%2==0 and n%3==0:   # 2와 3으로 모두 나누어 떨어지는 것은 n%2==0 and n%3==0으로 검사할 수 있다.   # 만약  n%2==0 and n%3==0 이면
    print("2와 3으로 나누어 떨어집니다.")   # 이를 출력하라.
else :   # 이 외의 경우라면
    print("2와 3으로 나누어 떨어지지 않습니다.")   # 이를 출력하라.




## 제 5장 연습문제7
# - 두자리 숫자로 이루어진 복권이 있다. 사용자가 가지고 있는 복권 번호 2자리 모두 일치하면 100만원을 받는다. 2자리 중에서 하나만 일치하면 50만원을 받는다.
#   하나도 일치하지 않으면 상금은 없다. 복권 당첨 번호는 난수로 생성하고 사용자의 입력에 따라서 상금이 얼마인지를 출력하는 프로그램을 작성하라.

import random   # 랜덤 모듈을 불러온다.
solution = random.randint(0, 99)   # randint(a,b)함수는 a이상, b이하의 범위에서 임의의 정수를 골라 돌려준다.
user = int(input("복권번호를 입력하시오(0에서 99사이): "))   # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력.
digit1 = solution // 10   # 숫자(digit), 복권 당첨 번호1, 각 자리수는 // 연산자와 % 연산자로 계산할 수 있다.
digit2 = solution % 10   # 복권 당첨 번호2
n1 = user // 10   # 사용자가 고른 번호1
n2 = user % 10   # 사용자가 고른 번호2

print("당첨 번호는 ", solution, " 입니다.")

if (digit1 == n1 and digit2 == n2):   # 만약 복권 당첨 번호1,2와 사용자가 고른 번호1,2가 같을 경우,
    print("상금은 100만원입니다.")   # 이를 출력하라.
elif (digit1 == n1   # 만약 복권 당첨번호 1과 사용자가 고른 번호 1이 같을 경우나
        or digit1 == n2   # 또는 복권 당첨번호 1과 사용자가 고른 번호 2가 같을 경우,
        or digit2 == n1   # 또는 복권 당첨번호 2와 사용자가 고른 번호 1이 같을 경우,
        or digit2 == n2):   # 또는 복권 당첨번호 2와 사용자가 고른 번호 2가 같을 경우,
    print("상금은 50만원입니다.")   # 이를 출력하라.
else:   # 이 외의 경우에는 
    print("상금은 없습니다.")   # 이를 출력하라.




## 제 5장 연습문제8
# - 사용자로부터 2개인 원에 대한 정보를 받아서 화면에 원을 그린 후에 조건문을 사용하여 큰 원 안에 작은 원이 포함되는지를 판단하는 프로그램을 작성하라.
#   큰 원의 중심좌표 x1: 0
#   큰 원의 중심좌표 y1: 0
#   큰 원의 반지름: 100
#   작은 원의 중심좌표 x2: 10
#   작은 원의 중심좌표 y2: 10
#   작은 원의 반지름: 50


import turtle   # 터틀 모듈을 불러온다.
t = turtle.Turtle()   # turtle을 t로 선언한다.
t.shape("turtle")   # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

x1 = int(input("큰 원의 중심좌표 x1: "))   # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력. x1의 값 입력.
y1 = int(input("큰 원의 중심좌표 y1: "))   # y1의 값 입력.
r1 = int(input("큰 원의 반지름: "))   # r1의 값 입력.
x2 = int(input("작은 원의 중심좌표 x2: "))   # x2의 값 입력.
y2 = int(input("작은 원의 중심좌표 y2: "))   # y2의 값 입력.
r2 = int(input("작은 원의 반지름: "))   # r2의 값 입력.

t.up()   # 펜을 든다.
t.goto(x1, y1)   # (x1, y1)으로 이동한다.
t.down()   # 펜을 내려놓는다.
t.circle(r1)   # 반지름이 r1인 원을 그린다.

t.up()   # 펜을 든다.
t.goto(x2, y2)   # (x2, y2)으로 이동한다.
t.down()   # 펜을 내려놓는다.
t.circle(r2)   # 반지름이 r2인 원을 그린다.

dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5   # 거리(distance), 맨 뒤의 0.5는 루트가 1/2제곱이기 때문에 0.5로 나타냄.
if dist <= r1 - r2:   # 원의 중심점 사이의 거리를 계산하고 이것을 (r1+r2)와 비교한다,   # 만약 거리가 r1-r2 이면
    turtle.write("두번째 원이 첫번째 원의 내부에 있습니다.")   # 이를 작성하라.
elif dist <= r1 + r2:   # 만약 거리가 r1+r2 이면
    turtle.write("두번째 원이 첫번째 원과 겹칩니다.")   # 이를 작성하라.
else:   # 그 외의 경우에는 
    turtle.write("두번째 원이 첫번째 원과 겹치지 않습니다.")   # 이를 작성하라.


