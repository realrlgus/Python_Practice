# 파이썬에서 문자열 만드는 방법
# 큰 따옴표
double_quotes = "Hello Python"
# 작은따옴표
single_qoutes = 'Hello Python'
# 삼중 큰 따옴표
triple_double_quotes = """Hello Python"""
# 삼중 작은따옴표
triple_single_quotes = '''Hello Python'''
# 삼중 큰, 작은 따옴표를 사용 시 다수의 라인이 포함된 문자열 작성 가능

# 문자열 연산 string = Python is fun!
head = "Python"
tail = " is fun!"
string = head + tail
print(string)

# 문자열 곱하기 =이 50번 출력
print("=" * 50)

# 문자열 인덱싱 twelve = s, back = n 마이너스 일경우 뒤에서부터 시작
phrase = "Life is too short, You need Python"
twelve = phrase[12]
back = phrase[-1]
print(twelve, back)

# 문자열 슬라이싱  one_three = Lif 끝번호에 해당되는것은 포함되지 않음 0:4 ==> 0 <= a < 3
one_three = phrase[0:4]
after_nineteen = phrase[19:]
before_seventeen = phrase[:17]
all_string = phrase[:]
print(one_three, after_nineteen, before_seventeen, all_string)

# 문자열 포매팅 문자열 내에 값을 삽입함
formmating_number = "I eat %d apples." % 3
formmating_string = "I eat %s apples." % "three"
num = 3
formmating_variable = "I eat %d apples." % num
day = "three"
formmating_many = "I ate %d apples. so i was sick for %s days." % (num, day)

# 고급 문자열 포매팅
advance_formmating = "I eat {0} apples.".format(num)

print(formmating_number, formmating_string,
      formmating_variable,  formmating_many, advance_formmating)

# 문자열 관련 함수
# 문자 개수 세기(count) a.count("b") = 2
a = "hobby"
print(a.count("b"))

# 문자 위치 알려주기(find) a.find('a') = -1 해당하는 문자의 인덱스 값 반환 없을경우 -1반환
# 문자 위치 알려주기(index) 해당하는 문자열을 찾지 못할경우 에러 발생
a = "Python!"
print(a.find('a'))

# 문자열을 대문자로 변경(upper) 소문자로 변경(lower) HI
a = "hi"
b = "HI"
print(a.upper())
print(b.lower())

# 문자열 공백 제거 lstrip rstrip strip 왼쪽 오른쪽 양쪽
a = " hi"
b = "hi "
c = " hi "
print(a.lstrip())
print(b.rstrip())
print(c.strip())

# 문자열 왼쪽 오른쪽 가운데 정렬
right = "{0:<10}".format("hi")
left = "{0:>10}".format("hi")
center = "{0:^10}".format("hi")
print(right, left, center)
