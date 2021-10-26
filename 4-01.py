## 제 4장 자료의 종류 : 도전문제1
# - 사각형의 각 변에 "안녕하세요? 홍길동씨, 터틀 인사드립니다." 를 출력해보자.

import turtle   # 터틀 모듈을 불러온다.
t = turtle.Turtle()   # 터틀을 t로 선언
t.shape("turtle");   # 터틀 모듈의 아이콘을 거북이 모양으로 선언, 명령어를 마칠 땐 ; 사용

s = turtle.textinput("","이름을 입력하시오: ")   # textinput()함수는 문자열을 입력할 수 있는 입력창을 생성한다.

for i in range(4):   # for 변수 in range() 는 변수를 괄호 안에 있는 숫자 만큼 반복해준다.
    t.write("안녕하세요? " + s +"씨, 터틀 인사드립니다.")   # 변수명.write("내용")
    t.left(90)   # 왼쪽으로 회전
    t.forward(100)   # 100픽셀 앞으로 이동
