## 제 10장 연습문제1
# 다음과 같이 하나의 레이블과 2개의 버튼을 가지는 프로그램을 작성해보자.

# 텍스트는 Label()로 생성한다. 버튼은 Button()으로 생성한다. 배치 관리자는 pack으로 한다.

from tkinter import Tk, Label, Button    # tkinter 모듈에 있는 모든 함수를 불러온다.

def greet():    # 환영하는 함수
    print("파이썬에 오신 것을 환영합니다.")    # 이를 출력하라.
    
window = Tk()    # 최상위 윈도우를 생성한다. tkinter 모듈 안의 Tk클래스가 하나의 윈도우이고, Tk클래스이 객체를 생성하면 화면에 윈도우가 나타난다.
label = Label(window, text = "간단한 GUI 프로그램!")    # 텍스트는 Label()로 생성한다.
label.pack()    # 텍스트 배치

greet_button = Button(window, text = "환영합니다.", command = greet)    # 환영 버튼, 버튼에는 text가 쓰이고, 버튼을 누르면 greet을 명령함.    # 버튼은 Button()으로 생성한다.
greet_button.pack()    # greet 버튼을 배치

close_button = Button(window, text = "종료", command = window.quit)     # 닫기버튼, 버튼에는 text가 쓰이고, 버튼을 누르면 window.quit를 명령함.
close_button.pack()    # 닫기버튼 배치

window.mainloop()    # 윈도우에서 발생하는 이벤트를 처리하는 코드, 마우스 클릭되어 버튼이 눌리는 이벤트를 처리.





## 제 10장 연습문제2
# 숫자를 입력하고 "더하기" 버튼을 누르면 합계에 더해지고, "빼기" 버튼을 누르면 합계에서 빼지는 계산기를 작성해본다.

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E    # tkinter 모듈에 있는 모든 함수를 불어온다. 

def update_add():    # 더하기(add)를 갱신하는 함수
    update("add")    
 
def update_subtract():    # 빼기(subtract)를 갱신하는 함수
    update("subtract")
 
def update_reset():    # 초기화(reset)를 갱신하는 함수 
    update("reset")
 
window = Tk()    # 최상위 윈도우를 설정한다.
total = 0    # 합계 변수를 0으로 선언
sum = Label(window)    # 합을 텍스트로 생성.  # 텍스트는 Label()로 생성한다.
sum.grid(row=0, column=1, columnspan=2)    # 합(sum), 격자(grid), 가로(row), 세로(column), 폭(span)

label = Label(window, text = "현재 합계: ")    # 라벨 # 텍스트는 Label()로 생성한다.
label.grid(row=0, column=0)    # label의 격자(가로0, 세로0)

entry = Entry(window)    # 들어가다(entry), 윈도우를 들어감.
entry.grid(row=1, column=0, columnspan=3)    # entry의 격자(가로1, 세로0, 폭3)

add_button = Button(window, text = "더하기(+)", command=update_add)    # 버튼은 Button()으로 생성한다.   # 더하기(add) 버튼, 버튼에는 text가 쓰이고, 버튼을 누르면 update_add를 명령함.
subtract_button = Button(window, text = "빼기(-)", command=update_subtract)    # 빼기(subtract) 버튼, 버튼에는 text가 쓰이고, 버튼을 누르면 update_subtract를 명령함.
reset_button = Button(window, text = "초기화", command=update_reset)    # 초기화(reset) 버튼, 버튼에는 text가 쓰이고, 버튼을 누르면 update_reset을 명령함.

add_button.grid(row=2, column=0)    # 더하기버튼 격자(가로2 세로0)
subtract_button.grid(row=2, column=1)   # 빼기버튼 격자(가로2 세로1)
reset_button.grid(row=2, column=2)    # 초기화버튼 격자(가로2 세로2)

def update(method):    # 방법(method)을 갱신하는 함수 
    global total    # 전역변수 합계
    if method == "add":    # 만약 방법이 더하기라면,
        total += int(entry.get())    # 합계는, 입력받은 수를 더한 값   # int()는 문자열을 숫자로 바꾼다.
    elif method == "subtract":    # 만약 방법이 빼기라면, 
        total -= int(entry.get())    # 합계는, 입력받은 수를 뺀 값    # int()는 문자열을 숫자로 바꾼다.
    else:     # 이 외의 경우라면
        total = 0    # 합계는 0이다.
    sum['text'] = str(total)    # 정수 변수는 str()을 적용하여 문자열로 변환가능하다.
    entry.delete(0, END)    # 입력받은 값 지우기

window.mainloop()     # 윈도우에서 발생하는 이벤트를 처리하는 코드, 마우스 클릭되어 버튼이 눌리는 이벤트를 처리.





## 제 10장 연습문제3
# 우리가 앞에서 텍스트 버전으로 제작하였던 숫자 맞추기 게임을 그래픽 사용자 인터페이스 버전으로 작성해보자.

import random    # 랜덤모듈을 불러온다.
from tkinter import *    #tkinter의 모든 함수를 불러온다.

window = Tk()    # 최상위 윈도우를 설정한다.
secret_number = random.randint(1, 100)    # 비밀 숫자 랜덤,  # randint(a,b)함수는 a이상 b이하의 범위에서 임의의 정수를 골라 돌려준다.
guess = None    # 추측이 아무것도 없음,
num_guesses = 0    # 추측하는 숫자 0

def guess_number():    # 숫자를 추측하는 함수
    global num_guesses    # 전역변수 추측하는 숫자
    guess = int(entry.get())    # 입력받는다.
    num_guesses += 1    
    if guess == secret_number:    # 만약 guess와 비밀 숫자가 같다면
        message = "축하합니다!!"    # 이 메세지를 띄운다.
    elif guess < secret_number:    # 만약 guess보다 비밀 숫자가 크다면
        message = "너무 낮아요!!"    # 이 메세지를 띄운다.
    else:    # 이 외의 경우라면
        message = "너무 높아요!!"    # guess의 값이 너무 높다는 메세지를 띄운다.
    label['text']= message

def reset():    # 초기화 함수
    global num_guesses    # 전역변수 추측하는 숫자
    entry.delete(0, END)    # 입력받은 수를 지운다.
    secret_number = random.randint(1, 100)     # 비밀 숫자 랜덤,  # randint(a,b)함수는 a이상 b이하의 범위에서 임의의 정수를 골라 돌려준다.
    guess = 0    # guess를 0으로 설정 
    num_guesses = 0    # 추측하는 수가 0이면
    message = "1부터 100사이의 숫자를 추측하시오."   # 이 메세지를 띄운다.
    label['text']= message    
    
message = "1부터 100사이의 숫자를 추측하시오."    # 메세지 변수
label = Label(window, text=message)    # 윈도우에 텍스트 생성
entry = Entry(window)    # 윈도우를 들어감.

guess_button = Button(window, text = "숫자를 입력", command=guess_number)    # 버튼은 Button()으로 생성한다.   # 추측(guess) 버튼, 버튼에는 text가 쓰이고, 버튼을 누르면 guess_number을 명령함.
reset_button = Button(window, text = "게임을 다시 실행", command=reset)    # 초기화(reset) 버튼, 버튼에는 text가 쓰이고, 버튼을 누르면 reset을 명령함.

label.grid(row=0, column=0, columnspan=2, sticky=W+E)    # 텍스트 격자( 가로0, 세로0 폭2 sticky=W+E)
entry.grid(row=1, column=0, columnspan=2, sticky=W+E)    # entry 격자( 가로1 세로0 폭2 sticky=W+E)
guess_button.grid(row=2, column=0)    # 추측 버튼 격자( 가로2 세로0)
reset_button.grid(row=2, column=1)    # 초기화 버튼 격자( 가로0 세로1)


window.mainloop()    # 윈도우에서 발생하는 이벤트를 처리하는 코드, 마우스 클릭되어 버튼이 눌리는 이벤트를 처리.
