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