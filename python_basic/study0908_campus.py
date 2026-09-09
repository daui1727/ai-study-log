# [ 튜플(Tuple) ]
# 리스트와 형태는 같지만, 한번 정해진 요소는 변경할 수 없다. 함수의 리턴 값을 여러 개 담아 보낼 때 주로 사용된다.

tuple_test03 = (10, 20, 30)
tuple_test03[0]
print(tuple_test03)  # (10, 20, 30)
print(tuple_test03[0]) # 10

# ! 요소가 하나 뿐인 튜플
# (273) - 그냥 정수 273(괄호로 감싼 것 뿐) /  (273,) - 쉼표가 필수고 진짜 튜플

# 괄호 없는 튜플 -> 다중 할당 & 값 교환하기(swap) - 임시 변수 없이 한줄로 가능하다
a1, b1, c1 = 10, 20, 30
a1, b1 = b1, a1
print(a1, b1)  # 20 10

# 튜플과 함수
def test03():
    return (50, 60) # 여러 값을 한 번에 리턴한다

a2, b2 = test03()
print(a2, b2)  # 50 60

# enumerate(리스트) -> (인덱스, 값) 튜플을 순서대로 반환한다
# divmod(a, b) -> (몫, 나머지) 를 튜플로 한번에 반환한다

for i, value in enumerate([5, 6, 7]):
    print(i, value)
# 0 5
# 1 6
# 2 7
x, y = divmod(100,3) # 33 1

# [ 콜백 함수(Callback)와 람다(lambda) ]
# 함수를 다른 함수의 매개변수로 넘겨서 진행되는 함수

# map() / filter() - 대표적인 콜백 함수 - 아래에 예시
# map(), filter() 결과는 제너레이터라서 list()로 감싸야 눈에 보인다.


# ==========================================================================================
# 우리는 프레임워크나 모듈을 왜 사용할까?
''' 프레임워크나 모듈은 이미 만들어진 기능과 구조를 활용해서(정형화)(재사용성)
개발 시간과 반복 작업을 줄이고, 더 효율적으로 프로그램을 만들기 위해서 입니다.

모듈 -> 필요한 기능을 가져다 씀
프레임워크 -> 프로그램을 만들기 위한 전체적인 구조와 기능을 활용함
'''

# [표준 모듈]
# math 모듈의 주요함수
import math
math.sin(1)
math.cos(1)
math.tan(1)
math.floor(2.5)
math.log(100,10)
math.ceil(2.5)

print()

# round() 함수 - 은행가 반올림 : 정수 부분이 짝수일 때 소수점이 5면 내리고 홀수일 때 5면 올린다
print(round(1.5))
print(round(2.5))

print()

# 매번 math. 를 붙이기 힘들다면 from 구문을 사용
from math import sin,cos,tan
print(sin(1))

print()

# from math import * - 모두 가져오기

# import math as m - 모듈 이름이 길거나 충돌이 걱정일 때 사용

# random 모듈 - 랜덤

# sys 모듈 - 시스템 관련 정보
# import sys
# print(sys.argv)
# sys.exit()

# python module_sys.py 10 20 30 - 실행하면 sys.argv에 ['module_sys.py', '10', '20', '30']라는 리스트가 담긴다.
# ['module_sys.py', '10', '20', '30'] -> 명령 매개변수(입력한 명령어에 따라 달라진다)

# os 모듈 - 운영체제 관련 기능
# os.system() 명령어를 그대로 실행시키기 때문에 주의할 것.

# datetime 모듈 - 날짜와 시간 다루기
import datetime
print("현재 시각 출력하기")
now = datetime.datetime.now()
print(f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분")

print()

# time 모듈 - 시간 정지 등
import time
print("지금부터 5초 동안 정지!")
time.sleep(5)
print("프로그램을 종료합니다")

print()

# urllib 모듈 - URL(인터넷 주소) 다루기
# URL = Uniform Resource Locator, 네트워크 자원의 위치, 웹브라우저 주소
# 모듈을 읽어 들입니다..
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("https://google.com")
output = target.read()# 출력합니다.
#print(output)
# 결과 앞에 붙는 b는 "binary data". urlopen()으로 페이지를 열고 read()로 내용을 읽어온다

# [파일 열기]
# file = open("basic.txt", "w", encoding="utf-8")
# file.write("파이썬 파일 처리 예제 작성 중....")
# file.close()





# =============================================================================================
'''
1. 파이썬 = 튜플(tuple), 람다(lambda)

튜플 : 함수와 함께 사용되는 리스트와 비슷한 자료형
     리스트와 차이점 - 한번 결정된 요소는 바꿀 수 없다

() 사용


람다 : 매개변수로 함수를 전달하기 위해 함수 구문을 작성하는
     것이 번거롭고, 코드 낭비라 생각이 들 때 함수를 간단
     하고 쉽게 선언하는 방법  ()->{} 1회용 함수를 만들 때
     사용한다.

함수를 매개변수로 사용하는 대표적인 표준 함수(filter(), map())
filter(함수, 리스트) - 리스트의 요소를 함수에 넣고 리턴값이 True인 값만 밖으로 빼낸다.

map(함수, 리스트) - 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수


lambda 매개변수 : 리턴값

파일처리 
- 텍스트 파일
- 바이너리 파일

파일을 처리하려면
1. 파일을 생성하거나 열기(open) -> 파일 읽기, 파일 쓰기
     - open(파일의 경로, mode)
       mode : w,a,r

     - close()
     - with 키워드 파일의 열고 닫지 않는 실수를 방지하기 위한 태그

'''
# =============================================================================================

# 콜백 함수
def call_10_times(func):
    for i in range(10):
        func() # 이 부분이 실행될 때마다 hello가 나온다

def print_hello():
    print("hello")

call_10_times(print_hello) # ()가 있느냐 없느냐로 지금 실행할지 데이터로 전달해서 실행할지가 정해지는 것
# 함수에서 함수를 부르는 콜백 함수. 자동화
print()

# 함수를 선언한다.
def power(item):
    return item*item

def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

# map 함수 사용
output_a = map(power, list_input_a)
print("output_a : ", output_a)
print("output_a : ", list(output_a))

print()

#filter()
output_b = filter(under_3, list_input_a)
print("output_b : ", output_b)
print("output_b : ", list(output_b))

# 0x000002D106E05C90 이런 형태를 제너레이터라고 부른다
print()

# 람다 lambda
power = lambda x: x*x
under_3 = lambda x: x<3

list_a = [1,2,3,4,5]
# map 함수
output_a = map(power, list_a)
output_b = filter(under_3, list_a)

print("output_a : ", list(output_a))
print("output_b : ", list(output_b))

output_a = map(lambda x: x*x, list_a)
output_b = filter(lambda x: x>3, list_a)

print()
print("output_a : ", list(output_a))
print("output_b : ", list(output_b))
print()
#============================

# 튜플 tuple
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a : ", a)
print("b : ", b)
print("c : ", c)
print("d : ", d)
print()
# 튜플은 함수의 리턴에 많이 사용된다.
# test 함수 선언하고, test 함수는 return 값으로 10, 20
# 두 개의 정수를 리턴한다.
def test2():
    return 100
def test():
    return 10, 20
def test1():
    return 30, 40

print(test())
a,b = test1()
print(f"{a}, {b}")
print()
print("실무 예제 for  enumerate()")

for i, value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는 {}입니다.".format(i+1, value))

print()

# =======================================================

tuple_test = 10, 20, 30, 40
print("괄호가 없는 튜플 값과 자료형 출력")
print("tuple_test : ", type(tuple_test))

# 괄호가 없는 튜플 테스트 tuple_test01에 자신의 이름과 친구
# 2명의 이름 할당 출력
tuple_test01 = "다람쥐","오소리","당나귀"
print("친구들 : ", tuple_test01[0])
print("친구들 : ", tuple_test01[1])
print("친구들 : ", tuple_test01[2])

for name in tuple_test01:
    print(f"이름 : {name}")

print()

# a, b에 튜플 10, 20 값을 할당해주세요.
a, b = 40, 50
print("교환 전 값 a : ", a)
print("교환 전 값 b : ", b)

a, b = b, a
print("교환 후 값 a : ", a)
print("교환 후 값 b : ", b)

#=============================================================

