## 제 11장 연습문제1
# 사용자가 입력한 텍스트 파일을 열어서 파일 안에 글자가 몇 개나 있는지를 계산하는 프로그램을 작성하라.

filename = input("파일 이름을 입력하세요: ").strip()    # 파일 이름, # input()은 사용자의 입력을 받아 출력한다.    # strip()는 문자열에서 양끝의 공백문자를 삭제한다.
infile = open(filename, "r") 
count = 0    # count를 0으로 초기화한다

for line in infile:    # for in은 반복문
    for ch in line:
        count += 1

print("파일 안에는 총 ", count , "개의 글자가 있습니다.")    # 이를 출력하라.
infile.close()    # 파일을 닫는다.





## 제 11장 연습문제2
# 사용자로부터 파일 이름과 삭제할 문자ㅐ열을 입력받는다. 파일을 열어서 사용자가 원하는 문자열을 삭제한 후에 다시 파일에 쓴다.

infilename = input("파일 이름을 입력하시오: ").strip()   # infile 이름, # input()은 사용자의 입력을 받아 출력한다.    # strip()는 문자열에서 양끝의 공백문자를 삭제한다.
infile = open(infilename, "r")    # infile을 연다.
file_s = infile.read()     # 파일을 읽는다. 
removed_s = input("삭제할 문자열을 입력하시오: ").strip()    # input()은 사용자의 입력을 받아 출력한다.    # strip()는 문자열에서 양끝의 공백문자를 삭제한다.
modified_s = file_s.replace(removed_s, "")

infile.close()     # infile을 닫는다.
outfile = open(infilename, "w")    # 파일을 연다

print(modified_s, file = outfile, end = "")     # 이를 출력하라.
print("변경된 파일이 저장되었습니다.")     # 이를 출력하라.
outfile.close()    # outfile을 닫는다.






## 제 11장 연습문제3
# 사용자가 입력하는 파일에 있는 각 문자들이 나타내는 빈도를 계산하는 프로그램을 작성하라.

infile = open(filename, "r")    # 텍스트 파일이므로 open(filename, "r")과 같이 파일을 연다.파일 안의 각 줄은 다음과 같이 읽을 수 있다. 각 줄 안의 문자들은 다시 for 루프를 이용하면 된다. 
for line in infile:    # for in 은 반복문
        ...
def countLine(line, counter):   # 빈도를 계산하는 함수
    for ch in line:
        if ch.isalpha():
                if ch in counter:
                        counter[ch] = counter[ch] + 1
                else:
                        counter[ch] = 1
                        
fname = input("입력 파일 이름: ").strip()
infile = open(fname, "r") 

my_dict = { } 
for line in infile:
        countLine(line, my_dict)
        
print(my_dict)
infile.close()     # 파일을 닫는다.
