
x = 10
under_20 = x < 20
print("under_20 : ", under_20)
print("not under_20 : ", not under_20)

#if 뒤에 불 값이 거짓인 경우
#명령문이 있어도 실행되지 않는다.
if True:
    print("참입니다")

if False:
    print("거짓입니다")
#실행 안된다.

# 조건문의 기본 사용
number = input("정수 입력>")
number = int(number)

if number > 0:
    print("양수입니다")

if number < 0:
    print("음수입니다")

if number == 0:
    print("0입니다")

#날짜/시간과 관련된 기능

import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

#format으로 시간 표현

import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year, now.month,
    now.day, now.hour,
    now.minute, now.second
    ))

#오전/오후 구분

import datetime

#현재 시간 정보를 불러오는 함수
now = datetime.datetime.now()

if now.hour > 12:
    print("현재시간은 {}시, 오후입니다".format(now.hour))

if now.hour < 12:
    print("현재시간은 {}시, 오전입니다".format(now.hour))

#계절을 구분하는 방법

import datetime

now = datetime.datetime.now()

#봄
if 3 <= now.month <= 5:
    print("지금은 {}월, 봄입니다.".format(now.month))

#여름