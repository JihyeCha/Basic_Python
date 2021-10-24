## 제 3장 - 도전문제4
# - 다음 프로그램에 주석을 붙여보자.
#   money = int(input("투입한 돈: "))
#   price = int(input("물건 값: "))

#   change = money - price
#   coin500s = change // 500
#   change = change % 500
#   coin100s = change // 100
#   change = change % 100

#   print("500원 동전의 개수: ", coin500s)
#   print("100원 동전의 개수: ", coin100s)

money = int(input("투입한 돈: "))   # 변수 money를 선언하고 정수형으로 받음
price = int(input("물건 값: "))     # 변수 price를 선언하고 정수형으로 받음

change = money - price     # 거스름돈을 계산
coin500s = change // 500   # 500으로 나눠서 몫이 500원짜리의 개수
change = change % 500      # 500으로 나눈 나머지를 계산
coin100s = change // 100   # 100으로 나눠서 몫이 100원짜리의 개수
change = change % 100      # 100으로 나눈 나머지를 계산

print("500원 동전의 개수: ", coin500s)   # 거슬러 줄 500원짜리의 개수를 출력
print("100원 동전의 개수: ", coin100s)   # 거슬러 줄 100원짜리의 개수를 출력



