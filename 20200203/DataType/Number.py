# <class 'int'> 모두 숫자형
a = 123
b = -123
c = 0
print(type(a), type(b), type(c))

# <class 'float'> 모두 실수형
a = 1.2
b = -3.45
print(type(a), type(b))

# <class 'float'> 파이썬 지수 표현 방식
a = 4.24E10
b = 4.24e-10
print(type(a), type(b))

# <class 'int'> a = 127 파이썬 8진수
a = 0o177
print(type(a), a)

a = 0x8ff
# <class 'int'> a = 2303 파이썬 16진수
print(type(a), a)

# 사칙연산 plus = 7, multiply = 12, divide = 0.75
# 파이썬 2.7 이후 버전은 정수형끼리 나누어도 실수값을 리턴함
a = 3
b = 4
plus = a + b
multiply = a * b
divide = a / b
print(plus, multiply, divide)

# 제곱 연산자 ** squared = 81
a = 3
b = 4
squared = a ** b
print(squared)

# 나머지 연산자 % remain = 81
a = 7
b = 3
remain = a % b
print(remain)

# 버리기 연산자 // floor = 1
a = 7
b = 4
floor = a // b
print(floor)
