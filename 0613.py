tuple_test = (10, 20, 30)
print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])
print()

#리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)

#출력
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

#괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("#괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(uple_test):", type(tuple_test))
print()

#괄호가 없는 튜플 활용
a, b, c = 10, 20, 30
print("#괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)
print()

a, b = 10, 20

print("# 교환 전 값")
print("a:",a)
print("b:",b)
print()

#값을 교환한다
a, b = b, a

print("# 교환 후 값")
print("a:",a)
print("b:",b)
print()

#파일을 연다(쓰기모드)
file = open("basic.txt", "w")

#파일에 텍스트를 쓴다.
file.write("Hello Python Programming...!")
#파일을 닫는다
file.close()

#파일 열기 (읽기모드)
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)

import random

hanguls = list("가나다라마바사아자차카타파하")

#파일을 쓰기모드로 열기
with open("info.txt", "w") as file:
    for i in range(1000):
        #랜덤 값으로 변수 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140,200)

        #텍스트를 쓴다.
        file.write("{}, {}, {}\n".format(name, weight, height))


with open ("info.txt", "r") as file:
    for line in file:
        #변수 선언
        (name, weight, height) = line.strip().split(", ")
        if (not name) or (not weight) or (not height):
            continue
        #결과 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"
        
        #출력
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}",
        ]).format(name, weight, height, bmi, result))
        print()