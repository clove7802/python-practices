example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

#딕셔너리의 items() 함수 결과 출력하기
print("#딕셔너리의 items()함수")
print("items():", example_dictionary.items())
print()

#for 반복문과 items()함수 조합해서 조합하기"
print("#딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

#리스트 변수 선언
array = []

#반복문을 적용합니다
for i in range(0, 20, 2):
    array.append(i * i)
print(array)

#리스트 안에서 for문 사용
array2 = [i * i for i in range(0, 20, 2)]
print(array2)

def print_n_times(value, n):
    for i in range(n):
        print(value)
print()

print_n_times("안녕하세요", 5)

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
            print()

print_n_times(3, "안녕하세요","즐거운", "파이썬 프로그래밍")

def print_n_times(value, n=2):
    for i in range(n):
        print(value)
    
print_n_times("안녕하세요")

# def print_n_times(n=2, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#             print()
# print_n_times("안녕하세요","즐거운","파이썬 프로그래밍")

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
            print()
print_n_times("안녕하세요","즐거운","파이썬 프로그래밍")

def return_test():
    return 100

value = return_test()

print(value)

def return_test():
    return

value = return_test()
print(value)
