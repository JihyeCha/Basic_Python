## 제 3장 - 도전문제3
# - 자판기가 만약 50원짜리 동전과 10원짜리 동전도 거슬러 줄 수 있다면 위 코드는 어떻게 수정하여야하는가?

#

money = int(input("투입한 돈: "))  # 변수 money를 선언하고 정수형으로 받음
price = int(input("물건 값: "))    # 변수 price를 선언하고 정수로 받음

change = money - price     # 거스름돈을 계산
print("거스름돈: ", change)
coin500s = change // 500   # 500으로 나눠서 몫이 500원짜리의 개수
change = change % 500      # 500으로 나눈 나머지를 계산
coin100s = change // 100   # 100으로 나눠서 몫이 100원짜리의 개수
change = change % 100      # 100으로 나눈 나머지를 계산
coin500s = change // 50    # 50으로 나눠서 몫이 50원짜리의 개수
change = change % 50       # 50으로 나눈 나머지를 계산
coin100s = change // 10    # 10으로 나눠서 몫이 10원짜리의 개수
change = change % 10       # 10으로 나눈 나머지를 계산

print("500원 동전의 개수: ", coin500s)   # 거슬러 줄 500원짜리의 개수 출력
print("100원 동전의 개수: ", coin100s)
print("50원 동전의 개수: ", coin50s)
print("10원 동전의 개수: ", coin10s)
