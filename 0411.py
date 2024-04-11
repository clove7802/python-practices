input_a = """
    안녕하세요
문자열의 함수를 알아봅니다
"""
print(input_a)

#의도하지 않은 줄바꿈과 문자열 양옆의 공백을 제거하는 strip()함수
print(input_a.strip())

#문자열이 알파벳이나 숫자로만 구성되어있는가 isalnum()함수
print("TraintA10".isalnum())

#문자열이 숫자로 인식될 수 있는 것인가 isdigit()함수
print("10".isdigit())

#특정 문자찾기. 왼쪽부터
output_a = "안녕안녕하세요".find("안녕")
print(output_a)

#특정 문자찾기. 오른쪽부터
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

#문자열 내부에 문자열이 있는지 확인하는 in 연산자
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")
print()

#불린, 불, Boolean = 참(True), 거짓(False)

#같다
print(10 == 100)
#다르다
print(10 != 100)
#보다 작다
print(10 < 100)
#보다 크다
print(10 > 100)
#작거나 같다
print(10 <= 100)
#크거나 같다
print(10 >= 100)
print()

#한글 비교 연산자 자음순서
print("가방" == "가방")
print("가방" != "하마")
print("가방" < "하마")
print("가방" > "하마")
print()

#범위 지정
x = 25
print(10 < x < 30)
print(40 < x < 60)
print()

#AND 연산자. 양쪽값이 참일경우만 참
#OR 연산자. 한쪽만 참일경우도 참
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

#IF조건문 파이썬은 괄호 없이 들여쓰기로 작성
if True:
    print("True입니다...!")
    print("정말 True입니다...!")
    
#False이기때문에 출력 안함
if False:
    print("False입니다")

#입력 받아서 if문으로 참 거짓 출력하기
number = input("정수 입력> ")
number = int(number)

#양수 조건
if number > 0:
    print("양수입니다")

#음수 조건
if number < 0:
    print("음수입니다")

#0 조건
if number == 0:
    print("0입니다")

#현재 시간 날짜 가져오기
import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))
