#숫자를 입력받습니다
number_input_a = int(input("정수 입력> "))

#출력합니다
print("원의 반지름:", number_input_a)
print("원의 둘례:", 2 * 3.14 * number_input_a)
print("원의 넓이:", 3.14 * number_input_a * number_input_a)

#try except 구문을 사용
try:
    file = open("info.txt", "w")
    #여러 가지 처리를 수행합니다.
    예외.발생해라() #예외
    #파일을 닫는다
    file.close()
except Exception as e:
    print(e)

print("#파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)