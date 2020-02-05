def plus(a, b):
    return a - b


def say_hello(name, age, are_from, fav_food):
    return f"Hello {name} you are {age} years old you are from {are_from} you like {fav_food}"


# output : -29 파이썬에선 인자의 순서 상관없이 인자명을 따라간다
result = plus(b=30, a=1)
print(result)

# 문자열 맨 앞에 f를 적고 문자열 안에 변수를 {}로 감싸면 문자열 포매팅이 됨
hello = say_hello("kihyeon", "21", fav_food="ramen", are_from="korea")
print(hello)
