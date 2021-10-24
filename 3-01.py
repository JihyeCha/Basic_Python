## 제 3장 계산해봅시다 : 도전문제1
# - 총 재료 비용이 100,000원이었다고 하자. 이익을 계산해보고 적자인지 흑자인지 표시하라.

# 총 재료 비용은 total로 표시 -> total = 

total = 100000
americano_price = 2000
cafelatte_price = 3000
smoothie_price = 3500

americanos = int(input("아메리카노 판매 수: "))
cafelattes = int(input("카페라떼 판매 수: "))
smoothies = int(input("스무디 판매 수: "))

sales = americanos * americano_price   # sales는 매출(량)
sales = sales + cafelattes * cafelatte_price
sales = sales + smoothies * smoothie_price
print("총 매출은 ", sales , "입니다.")

if(total < sales) : print("흑자")
else : print("적자")   # if문이 거짓일 때 실행문을 추가하고 싶으면 else 사용
