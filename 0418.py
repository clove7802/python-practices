import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

#오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

#오후 구분
if now.hour > 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

#봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

#여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

#가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을 입니다!".format(now.month))

#겨울 구분
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

number = input("정수 입력> ")

last_character = number[-1]
last_number = int(last_character)

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다")

number = input("정수 입력> ")
number = int(number)

#짝수 조건
if number % 2 == 0:
    print("짝수입니다")

#홀수 조건
if number % 2 == 1:
    print("홀수입니다")

now = datetime.datetime.now()
month = now.month


number = input("정수입력> ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")

if number % 2 == 1:
    print("홀수입니다")


if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")
    
#조건문으로 계절 확인
if 3 <= month <= 5:
    print("현재는 봄입니다")
elif 6 <= month <= 8:
    print("현재는 여름입니다")
elif 9 <= month <= 11:
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")