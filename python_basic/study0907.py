# def - 코드의 집합,  def 함수_이름(): 문장
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("Hello", 3)
# Hello
# Hello
# Hello

print()

# 가변 매개변수
def print_n_times(n, *values):    # n번 반복한다
    for i in range(n):
        for value in values: # values는 리스트처럼 활용
            print(value)

print_n_times(3, "안녕", "Hello", "Hi")

# 안녕
# Hello
# Hi
# 안녕
# Hello
# Hi
# 안녕
# Hello
# Hi

print()

# 키워드 매개변수
def print_n_times(*values, n=2):   # n=2는 기본 매개변수, 값을 입력하지 않으면 2를 기본으로 출력된다.
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("안녕하세요", "반갑습니다", "좋은 아침입니다", n=3) # 키워드 매개변수
# 안녕하세요
# 반갑습니다
# 좋은 아침입니다

# 안녕하세요
# 반갑습니다
# 좋은 아침입니다

# 안녕하세요
# 반갑습니다
# 좋은 아침입니다

print()

# return - 리턴은 함수를 실행했던 위치로 돌아가라는 의미와 끝내라는 의미를 가진다.
def return_test():
    print("1번")
    return # 리턴
    print("2번")

return_test()
# 1번

print()

# 정수를 더하는 함수
def sum_all(start=0, end=0, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i

    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))

# A. 550
# B. 5050
# C. 2550

print()

# 딕셔너리로 정보 조회하기
# 이름과 전공만 출력
student = {"이름": "김밥", "나이": 25, "전공": "요리"}

print(f"{student["이름"], student["전공"]}")
print()
# 이름 : 김밥, 전공 : 요리
noAge = ["이름", "전공"]

for i in noAge:
    print(f"{i} : {student[i]}")

# 이름 : 김밥
# 전공 : 요리

print()

# 학생 성적 관리 시스템
students = [      
        {"이름": "에어컨", "점수": 90},      
        {"이름": "선풍기", "점수": 75},  
        ]

def add_student(name, score):
        students.append({"이름": name, "점수": score})

def get_average():
    total = 0
    for i in range(len(students)):
        total += students[i]["점수"]

    return total / len(students)

def get_top_students():  # 평균 이상인 학생만 출력하는 함수
    top_students = []
    avg = get_average()

    for i in range(len(students)):
        if students[i]["점수"] > avg:
            top_students.append(students[i]["이름"])

    return top_students

add_student("비빔밥", 100)
print(students)
print(round(get_average()))
print(get_top_students())

# [{'이름': '에어컨', '점수': 90}, {'이름': '선풍기', '점수': 75}, {'이름': '비빔밥', '점수': 100}]
# 88
# ['에어컨', '비빔밥']

print()

