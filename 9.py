## 제 9장 도전문제1
# 편의점의 재고를 관리하는 프로그램을 만들어보자. 즉 재고를 증가, 또는 감소시킬 수 있도록 코드를 추가해보자. 간단한 메뉴도 만들어보자.

items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

while True:    # 어떤 조건이 만족될 때까지 반복하는 것은 while 루프이다. 만약 참이라면
    print("# 재고 목록 #")    # 이를 출력하라.
    for key in sorted(items.keys()):    # item의 재고
        print(key, items[key])    # 이를 출력하라.

    print("\n********************")    # 줄바꿈
    print("0. 종료")    # 이를 출력하라
    print("1. 재고 추가")    # 이를 출력하라
    print("2. 재고 삭제")    # 이를 출력하라.
    print("********************\n")     # 줄바꿈
    a = int(input("무엇을 하시겠습니까?: "))    # int()는 문자열을 숫자로 바꾼다. input()은 사용자의 입력을 받아 출력한다.
 
    if a == 1:     # 만약 a 가 1이라면
        item = input("물건의 이름을 입력하시오: ")    # input()은 사용자의 입력을 받아 출력한다.
        num = input("몇 개를 추가하시겠습니까? :")    # input()은 사용자의 입력을 받아 출력한다.
        items[item] = int(items[item]) + int(num)    # int()는 문자열을 숫자로 바꾼다.
    elif a == 2:    # 만약 a 가 2라면
        item = input("물건의 이름을 입력하시오: ")    # input()은 사용자의 입력을 받아 출력한다.
        num = input("몇 개를 삭제하시겠습니까? :")    # input()은 사용자의 입력을 받아 출력한다.
        items[item] = int(items[item]) - int(num)    # int()는 문자열을 숫자로 바꾼다.
    else:    # 이 외의 경우라면
        break    # 종료한다.





## 제 9장 도전문제2
# 영한사전이 아닌 한영사전을 만들려면 어떻게 해야하는가?

english_dict = dict()

english_dict['하나'] = 'one'
english_dict['둘'] = 'two'
english_dict['셋'] = 'three'

word = input("단어를 입력하시오: ")
print (english_dict[word])

# english_dict[''] = '' 에서 ['']와 뒤의 ''에 영어와 한글의 자리만 바꿔주면 된다.


