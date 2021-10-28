## 제 5장 - 도전문제7
# - import turtle
#   t = turtle.Turtle()
#   t.shape("turtle")
#
#   s = turtle.textinput("", "도형을 입력하시오: ")
#   if s == "사각형" :
#       s = turtle.textinput("", "가로: ")
#       w = int(s)
#       s = turtle.textinput("", "세로: ")
#       h = int(s)
#       t.forward(w)
#       t.left(90)
#       t.forward(h)
#       t.left(90)
#       t.forward(w)
#       t.left(90)
#       t.forward(h)
#   위의 프로그램에서 "사각형"만을 지원하고 있다. "삼각형","원"인 경우에 도형을 그리는 코드를 추가하라.

import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오: ")   # input()은 사용자의 입력을 받아 출력한다.
if s == "사각형" :   # 만약 사각형일 때
     s = turtle.textinput("", "가로: ")   # 가로 width, w,  # 가로 길이를 입력한다.
     w = int(s)
     s = turtle.textinput("", "세로: ")   # 세로 height, h,  # 세로 길이를 입력한다.
     h = int(s)
     t.forward(w)   # 가로로 지정한 픽셀만큼 직진
     t.left(90)   # 왼쪽으로 회전
     t.forward(h)   # 세로로 지정한 픽셀만큼 직진
     t.left(90)   
     t.forward(w)   
     t.left(90)
     t.forward(h)


elif s == "삼각형" :   # 만약 삼각형일 때
     s = turtle.textinput("", "한 변의 길이: ")   # 변  l,  # 한변의 길이를 입력한다.
     l = int(s)
     t.forward(l)   # 직진
     t.left(120)   # 정삼각형은 외각이 120도를 이뤄야 내각 60도가 만들어짐.
     t.forward(l)
     t.left(120)
     t.forward(l)   # "삼각형"의 경우


elif s == "원" :   # 만약 원일 때
     s = turtle.textinput("", "반지름: ")   # 반지름 radius, r,  # 반지름의 길이를 입력한다.
     r = int(s)
     t.circle(r)   # 반지름이 r인 원을 그린다.,  # "원"의 경우

