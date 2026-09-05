# 슬라이싱 [start:end:step] step은 몇 칸씩 이동할지
text = "abcdef"
print(list(text[1:4]))
# ['b', 'c', 'd'] 4번 전까지 가져온다

print(text[:4]) # abcd start 생략은 '처음부터' 가져온다는 뜻
print(text[2:]) # cdef end 생략은 '끝까지' 가져온다는 뜻
print(text[0:6:2]) # ace '2칸씩' 가져온다
print(text[::2]) # ace '처음부터' '끝까지' '2칸씩' 가져온다.
print(text[::-1]) # fedcba '거꾸로' 가져온다. 문자열이나 리스트 뒤집기에 사용된다
print(text[::-2]) # fdb 뒤에서부터 '거꾸로 2칸씩'
# 슬라이싱은 문자열"" 과 리스트[] 에서도 똑같이 쓰인다

# range(a, b, c)  a부터 b-1까지, c만큼의 차이를 두고 증가하는 정수 범위
print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8] 0부터 9까지 2만큼의 차이를 두고 가져온다

print(list(range(0, 10, 3)))
# [0, 3, 6, 9]

array = [111, 40, 222, 50, 333]
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i, array[i]))

# 0번째 반복 : 111
# 1번째 반복 : 40
# 2번째 반복 : 222
# 3번째 반복 : 50
# 4번째 반복 : 333

for i in range(4, -1, -1):
    print("반복 : {}".format(i))

# 반복 : 4
# 반복 : 3
# 반복 : 2
# 반복 : 1
# 반복 : 0

# reversed() 함수. list 등에도 적용 가능하다.
for i in reversed(range(5)):
    print("반복 : {}".format(i))

# 반복 : 4
# 반복 : 3
# 반복 : 2
# 반복 : 1
# 반복 : 0

# 피라미드 만들기
# 바깥쪽 반복문(i) : 줄바꿈(\n)과 몇 번째 줄인지 결정한다
# 안쪽 반복문(j) : 별(*)을 i번 만든다.
pyramid = ""

for i in range(1,6):
    for j in range(0, i):
        pyramid += "*"
    pyramid += "\n"
print(pyramid)

# *
# **
# ***
# ****
# *****

# 두번 중첩하지 않으면 이렇게 한번으로도 가능하다. 같은 피라미드 결과
pyramid_1 =""
for i in range(1,6):
    pyramid_1 += "*" * i + "\n"
print(pyramid_1)

# 바깥쪽 반복문(i) : 줄바꿈 담당
# 첫 번째 안쪽 반복문(j) : 공백 생성
# 두 번째 안쪽 반복문(k) : 별 생성
pyramid_2 =""

for i in range(1, 10):
    for j in range(9, i, -1):
        pyramid_2 += " "
    for k in range(0, 2 * i - 1):
        pyramid_2 += "*"

    pyramid_2 += "\n"
print(pyramid_2)

#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************

# import time

# number = 0
# seconds = time.time() + 10 # 10초 동안 반복한다

# while time.time() < seconds:
#     number += 1
#     # print("10초 동안 {}번 반복".format(number))

# # 10초 동안 3012824번 반복
i = 0

while True:
    print("{}번째 반복".format(i))
    i += 1
    input_text = input("종료하시겠습니까? (y/n) : ")
    if input_text in ["y", "Y"]:
        print("반복 종료")
        break

numbers = [10, 20, 30, 40, 50, 60]
for number in numbers:
    if number < 31:
        continue
    print(number, end=" ")
# 40 50 60

print()

# 두 리스트를 조합해 딕셔너리를 만들어라
key_list = ["number", "age", "color"]
value_list = [8, 35, "green"]

dict_a = {}

for i in range(len(key_list)):
    dict_a[key_list[i]] = value_list[i]

print(dict_a)
# {'number' : '8', 'age' : '35', 'color' : 'green'}

print()

# 1부터 10000이 넘는 순간을 구하고 그 때의 합계도 계산하기
limit = 10000
i = 1
sum_value = 0

while i < limit:
    sum_value += i
    i += 1
    if sum_value >= 10000:
        break

print("{}를 더할 때 {}을 넘고 그 때 값은 {}이다".format(i-1, limit, sum_value))

## 이렇게도 가능
limit_1 = 10000
j = 1
sum_value_1 = 0

while sum_value_1 < limit_1:
    sum_value_1 += j
    j += 1

print(f"{j-1}를 더할 때 {limit_1}을 넘고 그 때 값은 {sum_value_1}이다")

# 1~100까지의 숫자를 1 * 99, 2 * 98, 3 * 97, ..., 98 * 2, 99 * 1 식으로 계산한다면
# 최대가 되는 순간을 찾아보세요.
a = 0
b = 0
max_value = 0
for i in range(0, 100):
    j = 100 - i

    if i * j > max_value:
        max_value = i * j
        a = i
        b = j

print("최대 : {} *{} = {}".format(a, b, max_value))

