## 제 4장 - 도전문제4
# - str()을 사용하지 않고 print("올해는 ",thisYear,"입니다")와 같이 쉼표를 사용하여 변수와 문자열을 동시에 출력할 수 있는가?
#   위의 프로그램을 이런식으로 변경해보자.

import time   # time모듈을 불러온다.
 
 now = time.time()
 thisYear = int(1970 + now//(365*24*3600))   # 365일(1년)*24시간(하루)*3600초(1시간)

print("올해는 ",thisYear," 입니다")

age = int(input("몇 살이신가요?"))
print("2050년에는 ", (age+2050-thisYear),"살 이시군요.")

