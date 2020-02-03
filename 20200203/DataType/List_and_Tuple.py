# 리스트는 객체들의 순서가 있는 모임
# 리스트는 숫자 문자 혼합하여 사용 가능, 다중 리스트도 구현 가능함
listNum = [1, 2, 3, 4, 5]
listStr = ['I', 'My', 'Me', 'Mine']
listNumStr = [1, 'I', 30, 'You']
listList = [1, 'I', [30, 'You']]

# 리스트 요소 변경
listNum[2] = 100
print(listNum)

listNum[1:4] = 'x'
print(listNum)

# 리스트 요소 삭제
listStr[1:3] = []
print(listStr)

del listNumStr[0]
print(listNumStr)
# 리스트 삭제
del listStr

# 비어있는 리스트 생성
a = list()

# 리스트 더하기 -> 리스트가 병합됨 [1,2,3,4,5,6]
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 리스트 곱하기 -> 리스트가 반복되어 더해짐 [1,2,3,1,2,3,1,2,3]
a = [1, 2, 3]
print(a * 3)

# 리스트 관련 함수
# 리스트 요소 추가(append) 리스트 맨 뒤에 값을 붙임 [1,2,3,4]
a.append(4)
print(a)

# 리스트 정렬(sort) 오름차순으로 정렬해줌 [1,2,3,4]
b = [1, 4, 3, 2]
b.sort()
print(b)

# 리스트 정렬(reverse) 내림차순으로 정렬해줌 [4,3,2,1]
b.reverse()
print(b)

# 위치 반환(index) 값의 index를 반환함 a.index(3) = 2
a = [1, 2, 3]
print(a.index(3))

# 리스트 요소 삽입 insert(a,b) a번째 위치에 b를 삽입 [0,1,2,3]
a = [1, 2, 3]
print(a.insert(0, 4))

# 리스트 요소 제거 remove(x) 첫번째로 나오는 x를 제거 [4,2,3]
a.remove(1)
print(a)


# 튜플
# 튜플은  괄호로 둘러쌈 , 리스트와 거의 유사하지만 값 생성, 삭제 수정이 불가능함

t1 = (1, 2, 3)

# 튜플을 리스트로 리스트를 튜플로 변경 가능
# <class 'list'>
t1 = list(t1)
print(type(t1))
# <class 'tuple'>
t1 = tuple(t1)
print(type(t1))
