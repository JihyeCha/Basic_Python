## 제 9장 연습문제1
# 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 펑균을 계산하여 출력하는 프로그램을 작성해보자.

# 공백 리스트를 생성하고, 사용자에게서 받은 정수를 append()로 리스트에 추가한다. 리스트의 크기는 len(alist)을 사용. len()은 내장 함수로 사용

alist = []     # 리스트 변수
sum = 0    # 합(sum)은 0으로 초기화

for i in range(5):    # for 변수 in range()는 ()안의 수 만큼 반복해준다.
    i = int(input("정수를 입력하세요: "))    # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다.
    alist.append(i)    # 리스트의 맨 끝에 i를 추가한다.
    
for i in alist:
    sum += i
avg = sum/len(alist)    # 평균(average) = 합 / 리스트의 크기   # len()은 내장함수이다.
print("평균 = ", avg)    # 이를 출력하라.





## 제 9장 연습문제2
# 주사위를 던져서 나오는 값들의 빈도를 계산하는 프로그램을 작성해보자 즉 1, 2, 3, 4, 5, 6의 값이 각각 몇 번이나 나오는지를 계산한다. 난수 발생 함수와 리스트를 사용해보자.

import random    # 랜덤 모듈을 불러온다.
counters = [0, 0, 0, 0, 0, 0]    # 계산기, 계산하는 프로그램(counters)

for i in range(1000):     # for 변수 in range()는 ()안의 수 만큼 반복해준다.
    value = random.randint(0, 5)    # 값(value),    # randint(a,b)함수는 a이상, b이하의 범위에서 임의의 정수를 골라 돌려준다.
    counters[value] = counters[value] + 1    
 
for i in range(6):    # for 변수 in range()는 ()안의 수 만큼 반복해준다.
    print("주사위가 ", i+1, "인 경우는 ", counters[i], "번")    # 이를 출력하라.





## 제 9장 연습문제3
# 딕셔너리를 사용하여서 친구들의 이름과 전화번호를 저장해보자. 사용자로부터 친구들의 이름과 전화번호를 입력받고 딕셔너리에 저장한다. 이름을 입력하지 않고 엔터키를 치면 검색모드가 된다. 검색 모드에서는 친구들의 이름으로 전화번호를 검색할 수 있도록한다.

contacts = { }    # 연락(contact), 연락처

while True:    # while True: 문은 : 이하의 한 단계이상 들여쓰기한 동작을 사용자가 종료하기 전까지 무한 반복한다.
    name = input("(입력모드)이름을 입력하세요: ")    # 이름(name), input()은 사용자의 입력을 받아 출력한다.
    if not name:    # 만약 name이 아니면
            break;    # 끝낸다.
    tel = input("전화번호를 입력하세요: ")    # 전화번호(telephone number),  input()은 사용자의 입력을 받아 출력한다.
    contacts[name] = tel    # 전화번호(telephone number)

while True:    # while True: 문은 : 이하의 한 단계이상 들여쓰기한 동작을 사용자가 종료하기 전까지 무한 반복한다.
    name = input("(검색모드)이름을 입력하세요: ")    # input()은 사용자의 입력을 받아 출력한다.
    if not name:    # 만약 name이 아니면
            break;    # 끝낸다.
    if name in contacts :    # 만약 이름이 연락처에 있다면
            print(name, "의 전화번호는 ", contacts[name], " 입니다.")    # 이를 출력하라.
    else:    # 이 외의 경우 다시 반복





## 제 9장 연습문제4
# 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 사각형을 그리는 프로그램을 작상해보자.

import turtle    # 터틀 모듈을 불러온다.
import random    # 랜덤 모듈을 불어온다.
t = turtle.Turtle()    # turtle을 t로 선언한다.
t.shape("turtle")    # turtle 모듈의 아이콘을 거북이 모양으로 선언한다.

def draw_square(x, y, c):     # 사각형을 그리는 함수
    t.up()    # 펜을 든다.
    t.goto(x, y)    # (x, y)좌표로 이동한다.
    t.down()    # 펜을 내려놓는다.
    t.color("black", c)    # 선 색상을 검은색으로 지정한다.
    t.begin_fill()    # 채우기를 시작한다.
    t.fd(100)    # 앞(forward)으로 100 픽셀 이동
    t.lt(90)    # 왼쪽(left)으로 90도 회전
    t.fd(100)    # 앞으로 100픽셀 이동
    t.lt(90)    # 왼쪽으로 90도 회전
    t.fd(100)    # 앞으로 100픽셀 이동
    t.lt(90)    # 왼쪽으로 90도 회전
    t.fd(100)    # 앞으로 100픽셀 이동
    t.lt(90)    # 왼쪽으로 90도 회전
    t.end_fill()    # 채우기를 종료한다.
    
for c in ["yellow", "red", "purple", "blue"]:    # 색상을 리스트에 저장
    x = random.randint(-100, 100)    # randint(a,b)함수는 a이상, b이하의 범위에서 임의의 정수를 골라 돌려준다.
    y = random.randint(-100, 100)    # randint(a,b)함수는 a이상, b이하의 범위에서 임의의 정수를 골라 돌려준다.
    draw_square(x, y, c)    # draw_square(x, y, c)를 호출





## 제 9장 연습문제5
# 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 다각형을 그리는 프로그램을 작성해보자.

import turtle    # 터틀 모듈을 불러온다,
import random    # 랜덤 모듈을 불러온다.

t = turtle.Turtle()    # turtle을 t로 선언한다.
s = turtle.Screen()

def draw_shape(t, c, length, sides, x, y):   # 다각형을 그리는 함수
    t.up()    # 펜을 든다.
    t.goto(x, y)    # (x, y)좌표로 이동한다.
    t.down()    # 펜을 내려놓는다.
    t.fillcolor(c)    # 채우기 색상 c.
    angle = 360.0 / sides    # 각도를 360.0/sides 로 선언
    t.begin_fill()    # 채우기를 시작한다.
    for dist in range(sides):   
        t.fd(length)    # 앞으로 length 값 만큼 직진
        t.lt(angle)    # 왼쪽으로  앵글 각도만큼 회전
    t.end_fill()    # 채우기를 종료한다.

for i in range(10):    # 10번 반복한다.
    color = random.choice(['white', 'yellow', 'blue', 'skyblue', 'orange', 'green'])    # 색상은 []안에서 랜덤으로 선택
    side_length = random.randint(10, 100)    # randint(a,b)함수는 a이상 b이하의 범위에서 임의의 정수를 골라 돌려줌.
    sides = random.randint(3, 10)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_shape(t, color, side_length, sides, x, y)    # 다각형을 그린다.

    
    
    
    
## 제 9장 연습문제6
# 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 별을 랜덤한 위치에 그리는 프로그램을 작성해보자.

import turtle    # 터틀 모듈을 불러온다.
import random    # 랜덤 모듈을 불러온다.

t = turtle.Turtle()    # turtle을 t로 선언한다.
s = turtle.Screen()    # screen을 s로 선언한다.
s.bgcolor("black")    # 배경(background)색을 검은색으로 지정한다.

def draw_star(aturtle, color, side_length, x, y):    # 별을 그리는 함수
    aturtle.color(color)    # 색상
    aturtle.begin_fill()    # 채우기를 시작한다.
    aturtle.penup()    # 펜을 든다.
    aturtle.goto(x, y)    # (x,y) 좌표로 이동한다.
    aturtle.pendown()    # 펜을 내려놓는다.
    for i in range(5):    # 5번 반복한다.
        aturtle.fd(side_length)    # 앞(forward)으로 side length 값 만큼 이동
        aturtle.rt(144)    # 오른쪽으로 144도 회전
        aturtle.fd(side_length)    # 앞으로 side length 값 만큼 이동
    aturtle.end_fill()    # 채우기를 종료한다.
    
for i in range(20):    # 20번 반복한다.
    color = random.choice(['skyblue', 'white', 'blue', 'green', 'yellow', 'orange'])    # 색상은 []안에서 랜덤으로 선택
    side_length = random.randint(10, 100)    # randint(a,b)함수는 a이상 b이하의 범위에서 임의의 정수를 골라 돌려줌.
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_star(t, color, side_length, x, y)    # 별을 그린다.





## 제 9장 연습문제7
# 인터넷 도메인의 약자와 해당되는 국가를 딕셔너리에 저장해보자. 예를 들어서 "kr"은 대한민국으로 저장되어야 한다. 딕셔너리를 순회하면서 모든 키와 값을 출력하는 프로그램을 작성해보자.

domains = {"kr": "대한민국", "sk": "슬로바키아", "no": "노르웨이", "us": "미국", "jp": "일본", "hu": "헝가리", "de": "독일"}    # 도메인(domain),   # 인터넷 도메인의 약자와 해당되는 국가를 딕셔너리에 저장한다.
for k, v in domains.items():   
    print (k, ": ", v)    # 이를 출력하라.






## 제 9장 연습문제8
# 딕셔너리에 문제와 정답을 저장하고 하나씩 꺼내서 사용자에게 제시하는 프로그램을 작성해보자. 사용자는 문자열로 답해야 한다. 번호로는 답할 수는 없다.
# 사용자는 문자열로 답해야 한다. 번호로는 답할 수는 없다.

problems = {'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
                '변수': '데이터를 저장하는 메모리 공간',
                '함수': '작업을 수행하는 문장들의 집합에 이름을 붙인것',
                '리스트': '서로 관련이 없는 항목들의 모임',
             }

def show_words(problems):    # 문제를 보여주는 함수
    display_message = ""    # 제시하는 메세지
    i=1    # i값을 1로 선언
    for word in problems.keys():    # 문제의 단어를 반복
        display_message += "("+str(i)+")"    # str() 함수는 계산 결과와 문자열을 연결할 때 사용하는 함수이다. 계산한 값이 문자열로 변환되어 출력된다.
        display_message += word + " "
        i+=1   # i+=1 로 선언
    print(display_message)    # display_message를 출력하라.

for meaning in problems.values():    # 문제가 의미하는 것
    print("다음은 어떤 단어에 대한 설명일까요? ")    # 이를 출력하라.
    print("\""+meaning+"\"")    # 
    correct = False    # 답이 거짓이면
    while not correct:     # 어떤 조건이 만족될 때까지 반복하는 것은 while 루프이다. 답이 아니라면
        show_words(problems)    # 문제를 다시 보여줘라.
        guessed_word = input("")     # 추측하는 단어,    # input()은 사용자의 입력을 받아 출력한다.
        if problems[guessed_word] == meaning:    # 만약 문제를보고 추측한 단어와 문제가 의미했던 것이 같으면
            print("정답입니다. !")    # 정답이라고 출력하라.
            correct = True    # 답이 참
        else:    # 이 외의 경우라면
            print("정답이 아닙니다.")    # 정답이 아니라고 출력하라.

