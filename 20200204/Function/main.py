def say_hello():
    print("hello")


def say_name(who):
    print("hello",  who)


def plus(a, b):
    print(a + b)


def minus(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)


def arithmetic(a, b, sign):
    if(sign == "+"):
        return a + b
    elif(sign == "-"):
        return a - b
    elif(sign == "/"):
        return a / b
    elif(sign == "*"):
        return a * b
    else:
        return None


say_hello()
say_name("kihyeon")
plus(3, 4)
print(arithmetic(5, 4, "-"))
