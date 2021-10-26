## 제 5장 - 도전문제2
# -(1) 사용자가 "l" 또는 "left"를 입력하면 왼쪽으로 움직이고, "r" 또는 "right"를 입력하면 오른쪽으로 이동하도록 소스를 약간 변경해보자.
# -(2) 사용자가 "q" 또는 "quit"를 입력했을 때, 프로그램을 종료하도록 하라. 

import turtle   # 터틀 모듈을 불러온다.  
t = turtle.Turtle()   # 터틀을 t로 선언한다.
t. width(3)    # 거북이가 그리는 선의 두께를 3으로 한다.
t.shape("turtle")   # 터틀 모듈의 아이콘을 거북이 모양으로 선언
t.shapesize(3, 3)   # 거북이 아이콘 크기를 3배 확대한다.

while True:
     command = input("명령을 입력하시오: ")   # input()은 사용자의 입력을 받아 출력한다.
     if command == "l" or command == "left":   # 만약 "l" 이나 "left"를 입력하면 아래와 같이 출력하라.(왼쪽으로 이동)
         t.left(90)
         t.forward(100)   # 왼쪽으로 이동
     if command == "r" or command == "right":   # 만약 "r" 이나 "right"를 입력하면 아래와 같이 출력하라.(오른쪽으로 이동)
         t.right(90)
         t.forward(100)   #오른쪽으로 이동   # (1)     
             
     if command == "q" or command == "quit":   # 만약 "q" 이나 "quit"를 입력하면 아래와 같이 실행하라.(종료)
         break   # 종료   # (2)
