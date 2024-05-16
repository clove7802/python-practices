#반복문과 while 반복문
#반복문 범위 지정하여 처음부터 범위까지 반복
print("#반복문 범위 지정하여 처음부터 범위까지 반복")
for i in range(5):
    print(str(i) + "= 반복 변수")
print()

#반복문의 시작과 끝 범위를 지정하여 범위 반복
print("#반복문의 시작과 끝 범위를 지정하여 범위 반복")
for i in range(5,10):
    print(str(i) + "= 반복 변수")
print()

#반복문에 스텝 사용하기
print("#반복문에 스텝 사용하기")
for i in range(0,10,3):
    print(str(i) + "= 반복 변수")
print()

#반복문에 배열(리스트) 사용하기
print("#반복문에 배열(리스트) 사용하기")
array = [273,32,103,57,52]
for element in array:
    print(element)
print()

for i in range(len(array)):
    print("{}번째 반복: {}".format(i,array[i]))
print()

#반복문 반대로 사용하기
print("#반복문 반대로 사용하기")
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
print()

#무한 반복
#while True:
#    print(".", end="")

list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)
print(list_test)

import time
number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초동안 {}번 반복했습니다.".format(number))

i = 0
while True:
    print("{}번째 반복문입니다.".format(i))
    i = i + 1
    
    input_text = input(">종료하시겠습니까?(Y/N): ")
    if input_text in ["y","Y"]:
        print("반복을 종료합니다.")
        break

numbers = [5,15,6,20,7,25]

for number in numbers:
    if number < 10:
        continue
    print(number)

numbers = [103,52,273,32,77]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()

list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)
print("#reversed()함수")
print("reversed([1,2,3,4,5]):",list_reversed)
print("list(reversed([1,2,3,4,5])):",list(list_reversed))
print()

print("#reversed() 함수와 반복문")
print("for i in reversed([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-", i)