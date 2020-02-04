import random
com_list = ['가위', '바위', '보']

while True:
    me = input()
    com = random.choice(com_list)
    while me not in ['가위', '바위', '보']:
        me = input("가위 바위 보 중에 입력하세요\n")
        com = random.choice(com_list)
    if(me == "가위"):
        if(com == "가위"):
            print("비김")
        elif(com == "바위"):
            print("짐")
        else:
            print("이김")
    elif(me == "바위"):
        if(com == "가위"):
            print("이김")
        elif(com == "바위"):
            print("비김")
        else:
            print("짐")
    else:
        if(com == "가위"):
            print("이김")
        elif(com == "바위"):
            print("짐")
        else:
            print("비김")
    re = input("다시 시작할까요? [예/아니오]")

    while re not in ['예', '아니오']:
        re = input("다시 시작할까요? [예/아니오]")

    if(me == "아니오"):
        break
