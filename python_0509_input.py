
## input 함수 사용 예시
## 게임 아이디와 비번 입력하는 과정으로 만들어봄.

>>> user_name = input("아이디를 입력해주세요 : ")
아이디를 입력해주세요 : 나의본운동은
>>> print(user_name)
나의본운동은
>>> type(user_name)
<class 'str'>

>>> password = input("비밀번호를 입력해주세요 : ")
비밀번호를 입력해주세요 : 12345
>>> print(password)
12345
>>> type(password)
<class 'str'>
>>> 

## 문자열을 숫자로 변환해야 숫자 연산에 활용가능.
## python은 문자열은 문자열끼리 연산, 숫자는 숫자끼리 연산해야함.

## password type을 str에서 int와 float로 바꾸는 과정

>>> type(password)
<class 'str'>
>>> password
'12345'
>>> password = int(password)
>>> password
12345
>>> type(password)
<class 'int'>

>>> password = float(password)
>>> password
12345.0
>>> type(password)
<class 'float'>

## 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환할때
## 오류가 난다.

>>> a = 55.5
>>> a
'55.5'
>>> type(a)
<class 'str'>
>>> a = int(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a = int(a)
ValueError: invalid literal for int() with base 10: '55.5'

## class를 str에서 float로 변환하고 다시 int로 하면 된다.

>>> a = float(a)
>>> a
55.5
>>> a = int(a)
>>> a
55
>>> type(a)
<class 'int'>


