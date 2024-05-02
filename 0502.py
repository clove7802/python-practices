import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다")

score = 3.2#float(input("학점 입력 > "))

if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자")
elif 2.8 <= score < 3.5:
    print("일반인")
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= score < 1.75:
    print("불가촉천민")
elif 0.5 <= score < 1.0:
    print("자벌레")
elif 0 < score < 0.5:
    print("시대를 앞서가는 혁명의 씨앗")
else:
    print("메롱")

print("# if 조건문에  0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 false로 변환됩니다")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")

number = 3#input("정수 입력> ")
number = int(number)

if number > 0:
    pass
else:
    pass

array = [273, 32, 103, "문자열", True, False]
print(array)

print(array[0])
print(array[1])
print(array[2])
print(array[1:3])
print(array[::2])

array[0] = "변경"
print(array)

list_a = [273,32 ,103, "문자열", True, False]
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])

print(list_a[3])
print(list_a[3][0])

list_a = [[1, 2, 3], [4,5,6,], [7,8,9]]
print(list_a[1])
print(list_a[1][1])

list_a = [1,2,3]
list_b = [4,5,6]

print(list_a + list_b)
print(list_a * 3)

print(len(list_a))

#리스트 뒤에 요소 추가하기
print("#리스트 뒤에 요소 추가하기")
list_a = [1,2,3]
list_a.append(4)
list_a.append(5)

print(list_a)
print()

#리스트 중간에 요소 추가하기
print("#리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)
print()

#리스트에 여러 요소 한번에 추가하기
print("#리스트에 여러 요소 한번에 추가하기")
list_a = [1,2,3]
list_b = [4,5,6]
list_a.extend([4,5,6])#list_a 뒤에 4,5,6 추가
print(list_a)
print(list_a + list_b)

print(list_a) #list_a에 4,5,6이 추가되어 변화됨
print(list_b)
print()

#list_a에 list_b의 내용을 추가
print("#list_a에 list_b의 내용을 추가")
list_a.extend([list_b])
print(list_a)
print(list_b)
print()

#리스트에서 위치를 지정하여 요소 하나 제거하기
print("#리스트에서 위치를 지정하여 요소 하나 제거하기")
list_a = [0,1,2,3,4,5]

del list_a[1]#방법1
print("del list_a[1]:", list_a)

list_a.pop(2)#방법2
print("pop(2):", list_a)
print()

#요소를 값으로 제거하기
print("#요소를 값으로 제거하기")
list_a.remove(5)
print(list_a)#5라는 값이 삭제됨
print()

#요소를 모두 제거하는 clear() 함수
print("#요소를 모두 제거하는 clear()함수")
list_d = [0,1,2,3,4,5]
list_d.clear()
print(list_d)
print()

#리스트 내부에 있는지 확인하는 in/not in 연산자
print("#리스트 내부에 있는지 확인하는 in/not in 연산자")
list_a = [273,32,103,57,52]
print(273 in list_a)
print(99 in list_a)
print(100 in list_a)
print(52 in list_a)
print(273 not in list_a)
print(99 not in list_a)
print(100 not in list_a)
print(52 not in list_a)
print(not 273 in list_a)