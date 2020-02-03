# 딕셔너리 자료형
# 키-값 으로 값을 보관함 {Key1:Value1} Key는 변하지 않는 값 사용
# 딕셔너리의  키가 중복될경우 한 쌍이 무시됨
dic = {'name': '기현', 'phone': '01032637320', 'birth': '1024'}

# 키를 이용한 딕셔너리 접근방법
name = dic['name']
phone = dic['phone']
birth = dic['birth']
print(name, phone, birth)

# 딕셔너리 복사
new_dict = dic.copy()

# 딕셔너리 쌍 추가 {1:'b' , 'age' : 20} 추가
new_dict[1] = 'b'
new_dict['age'] = 20
print(new_dict)

# 딕셔너리 요소 삭제
del new_dict['age']

# 딕셔너리 관련 함수

# Key값을 딕셔널리로 리턴함 (keys) ['name', 'phone', 'birth', 1]
print(new_dict.keys())

# values값을 딕셔널리로 리턴함 (values) ['기현', '01032637320', '1024', 'b']
print(new_dict.values())

# key value 쌍을 튜플로 묶은 객체로 돌려줌 (item) [('name', '기현'), ('phone', '01032637320'), ('birth', '1024'), (1, 'b')]
print(new_dict.items())

# key value 쌍 모두 지우기(clear)
new_dict.clear()

# key값으로 value 값 받기(get) 20
print(new_dict.get('age'))
