#for 반복문
#리스트와 함께 사용하는 반복문
print("#리스트와 함께 사용하는 반복문")
array = [273,32,103,57,52]

for element in array:
    print(element)
print()

#문자열로도 사용가능
print("#문자열로도 사용가능")
for character in "안녕하세요":
    print("-",character)
print()

#딕셔너리와 반복문
#딕셔너리의 구성. 중괄호로 선언
dict_a = {"키A":10, #문자열을 키로 사용
          "키B":20,
          "키C":30,
          1:40, #숫자를 키로 사용
          False:5 #불값을 키로 사용
          }
dict_b = {'name':'어벤저스 엔드게임','type':'히어로 무비'} #한줄로 구성
print(dict_a["키A"],dict_b["name"])
print()

#딕셔너리의 요소에 접근하는 방법
print("#딕셔너리의 요소에 접근하는 방법")
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"], #딕셔너리안에 리스트를 넣는것도 가능
    "origin": "필리핀"
}
print("name", dictionary["name"])
print("type", dictionary["type"])
print("ingredient", dictionary["ingredient"])
print("ingredient[1]", dictionary["ingredient"][1]) #리스트 안의 요소 가져오기
print("origin", dictionary["origin"])
print()

#딕셔너리 값 바꾸기
print("#딕셔너리 값 바꾸기")
dictionary["name"] = "8D 건조 망고"
print("name:",dictionary["name"])
print()

#딕셔너리에 요소 추가하기
print("#딕셔너리에 요소 추가하기")
dictionary2 = {}
print("요소 추가 이전:", dictionary2)
dictionary2["name"] = "새로운 이름"
dictionary2["head"] = "새로운 정신"
dictionary2["body"] = "새로운 몸"
print("요소 추가 이후:", dictionary2)
print()

#딕셔너리의 요소 제거하기
print("#딕셔너리의 요소 제거하기")
dictionary3 = {
    "name": "7D 건조 망고",
    "type": "당절임"
}
print("요소 제거전:", dictionary3)
del dictionary3["name"]
del dictionary3["type"]
print("요소 제거 후: ", dictionary3)
print()

#딕셔너리 내부에 키가 있는지 확인하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin": "필리핀"
}
#key = input("> 접근하고자 하는 키: ")
key = "null"
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")