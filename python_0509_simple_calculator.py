## 더하기만 할줄 아는 계산기

'''
def plus(x, y):
	#print(' {} + {} = {}'.format(x, y, x + y))
	return None

def Add(x, y):
	return x + y


while True:
	number1 = int(input(' 첫 번째 수 : '))
	if number1 == 0:
		break
	number2 = int(input(' 두 번째 수 : '))

	plus(number1, number2)
	#print(' {} + {} = {}'.format(number1, number2, number1 + number2))

	retv = Add(number1, number2)
	print(' {} + {} = {}'.format(number1, number2, retv))
'''
## 초간단 계산기

def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x, y):
    return x*y

def Div(x, y):
    return (x//y)
    
while True:
    print(' **  간단 계산기 ** ')
    n1 = int(input(' 첫 번째 수 : '))
    if n1 == 0:
        break

    op = input(' [ + - * /] : ')

    n2 = int(input(' 두 번째 수 : '))

    if op == '+':
        res = Add(n1, n2)
    elif op == '-':
        res = Sub(n1, n2)
    elif op == '*':
        res = Mul(n1, n2)
    elif op == '/':
        res = Div(n1, n2)
    else:
        print(op, '없는 연산입니다.')

    print('{} {} {} = {}'.format(n1, op, n2, res))

    ## if res < 1, 올바른 결과가 나오지 않음
    # def Div 부분을 return float(x//y) 바꿔봄
    # 실수로 변환하여 나오게 하여도 0.0이 나옴
    # 1/2 가 0.5로 출력되지 않음
    


