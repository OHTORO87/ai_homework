Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("그냥 따라하기")
그냥 따라하기
>>> 
>>> print(10)
10
>>> 
>>> print(10, 20, 30)
10 20 30
>>> 
>>> print(10 20 30)
SyntaxError: invalid syntax
>>> print(2.7)
2.7
>>> 
>>> print(2.5, 7.4, 90.56)
2.5 7.4 90.56
>>> 
>>> print("정수를 출력합니다")
정수를 출력합니다
>>> 
>>> 10
10
>>> 
>>> 10, 30, 50
(10, 30, 50)
>>> 
>>> 100 200 300
SyntaxError: invalid syntax
>>> 
>>> type(10)
<class 'int'>
>>> 
>>> type(-35)
<class 'int'>
>>> 
>>> type(2000)
<class 'int'>
>>> 
>>> type(50), type(70), type(100)
(<class 'int'>, <class 'int'>, <class 'int'>)
>>> 
>>> type(3, 5, 7)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    type(3, 5, 7)
TypeError: type.__new__() argument 1 must be str, not int
>>> 
>>> print("실수를 출력합니다")
실수를 출력합니다
>>> 
>>> 2.5
2.5
>>> type(3.5)
<class 'float'>
>>> 
>>> print(2.5, 3.5, 6.78)
2.5 3.5 6.78
>>> 
>>> print(5.6)
5.6
>>> 
>>> "문자열을 출력합니다"
'문자열을 출력합니다'
>>> 
>>> 서울
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    서울
NameError: name '서울' is not defined
>>> "서울"
'서울'
>>> 
>>> '서울'
'서울'
>>> 
>>> print("\' '" 같아요")
      
SyntaxError: invalid syntax
>>> print("\'\"같아요")
'"같아요
>>> '"같아요
SyntaxError: EOL while scanning string literal
>>> 
>>> print("\'\"같아요")
'"같아요
>>> print("서울", "부산", "광주")
서울 부산 광주
>>> 
>>> "울산", "여수", "제주"
('울산', '여수', '제주')
>>> 
>>> type("대한민국")
<class 'str'>
>>> 
>>> type('korea')
<class 'str'>
>>> 
>>> 
>>> print("양주종코딩스쿨")
양주종코딩스쿨
>>> 
>>> print("코딩 파이썬 3일차 - 정수와 사칙 연산")
코딩 파이썬 3일차 - 정수와 사칙 연산
>>> 
>>> 20
20
>>> 50
50
>>> 
>>> 20, 30, 50, 100
(20, 30, 50, 100)
>>> 
>>> 10 20 30
SyntaxError: invalid syntax
>>> 
>>> 20+30
50
>>> 50-20
30
>>> 20/4
5.0
>>> 20//4
5
>>> 10/3
3.3333333333333335
>>> 10%3
1
>>> 20%3
2
>>> 20%2
0
>>> 
>>> 2*2
4
>>> 2*5
10
>>> 2*3
6
>>> 2**3
8
>>> 2**4
16
>>> 2*8
16
>>> 2*10
20
>>> 2**10
1024
>>> 
>>> 
>>> "잘보세요"
'잘보세요'
>>> "중요합니다"
'중요합니다'
>>> for i in range(0,22):
	print(2,"^",i,"=","2**i)
	      
SyntaxError: EOL while scanning string literal
>>> for i in range(0,11):
	print(2, "^", i, "=", 2**i)

	
2 ^ 0 = 1
2 ^ 1 = 2
2 ^ 2 = 4
2 ^ 3 = 8
2 ^ 4 = 16
2 ^ 5 = 32
2 ^ 6 = 64
2 ^ 7 = 128
2 ^ 8 = 256
2 ^ 9 = 512
2 ^ 10 = 1024
>>> 
>>> 2**8
256
>>> 
>>> 2**16
65536
>>> 2**24
16777216
>>> 2**32
4294967296
>>> 
>>> 2**10
1024
>>> 
>>> 2**20
1048576
>>> 2**30
1073741824
>>> 2**40
1099511627776
>>> 2**50
1125899906842624
>>> 
>>> print("복습합니다")
복습합니다
>>> 2*3
6
>>> 2**3
8
>>> 2**4
16
>>> 100/34
2.9411764705882355
>>> 
>>> 100/3
33.333333333333336
>>> 100//3
33
>>> 10%3
1
>>> 
>>> 2**8
256
>>> 
>>> 2**10
1024
>>> 