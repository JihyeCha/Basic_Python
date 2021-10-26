## 제 5장 - 도전문제3
# - import random
#   print("동전 던지기 게임을 시작합니다.")
#   coin = random.randrange(2)
#   if coin ==0 :
#      print("앞면입니다.")
#   else:
#      print("뒷면입니다.")
#   print("게임이 종료되었습니다.") 를 주사위 던지기 게임으로 변환해보자. random.randrange(6)하면 0에서 5까지의 정수를 랜덤하게 생성할 수 있다.

import random   # 랜덤 모듈을 불러온다.
print("주사위 던지기 게임을 시작합니다.")
dice = random.randrange(6)+1   # 주사위는 dice, # 주사위의 눈은 1부터 6까지이므로 +1을 해준다.
print("주사위 눈은 "+str(dice)+"입니다.")   # str() 함수는 계산 결과와 문자열을 연결할 때 사용하는 함수이다. 계산한 값이 문자열로 변환되어 출력된다.
print("게임이 종료되었습니다.")
