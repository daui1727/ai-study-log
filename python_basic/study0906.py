# 소수(prime number) 판별하기
num = 17
count = 0
for i in range(2, num):
    if num % i == 0:
        count += 1

if count == 0:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")
# 17은 소수입니다.

print()

# 버블 정렬로 리스트 오름차순으로 정렬하기
# sort()를 사용하지 않고 중첩 반복문으로 정렬할 것
numbers = [6, 1, 7, 2, 8]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:  # 내림차순일 땐 > < 만 바꾸면 된다.
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers) # [1, 2, 6, 7, 8]

print()

# 딕셔너리 리스트에서 최고 점수의 학생을 찾아라
students = [    
            {"name": "아침", "score": 89},    
            {"name": "점심", "score": 91},    
            {"name": "저녁", "score": 67},
            ]

max_score = 0
best_student = ""

for student in students:
    if student["score"] > max_score:
        max_score = student["score"]
        best_student = student["name"]

print(max_score, best_student) # 91 점심

print()

# 위 문제를 높은 점수 순으로 sort()를 이용해 정렬한다면?
def get_score(student):
    return student["score"]

students.sort(key=get_score, reverse=True)
print(students) # [{'name': '점심', 'score': 91}, {'name': '아침', 'score': 89}, {'name': '저녁', 'score': 67}]

print()

# 학생 성적 데이터에서 과목별 평균 구하기
students = [    
            {"name": "아침", "korean": 82, "math": 100, "english": 95},    
            {"name": "점심", "korean": 92, "math": 50, "english": 88},    
            {"name": "저녁", "korean": 71, "math": 61, "english": 65},
            ]

korean_sum = 0
math_sum = 0
english_sum = 0

for student in students:
    korean_sum += student["korean"]
    math_sum += student["math"]
    english_sum += student["english"]

korean_avg = round(korean_sum / len(students))
math_avg = round(math_sum / len(students))
english_avg = round(english_sum / len(students))

print("국어 평균:", korean_avg)
print("수학 평균:", math_avg)
print("영어 평균:", english_avg)

print()

# 문자열
# len() - 글자 수 세기
# .upper() .lower()
# .strip()
user_input = "   몇 글자일까요?   "
print("1",len(user_input)) # 1 14
print(user_input.strip())  # 출력: "몇 글자일까요?" (양옆 공백 삭제)
user_input = user_input.strip()
print("2",len(user_input)) # 2 8

# .split() - 구분자로 잘라서 리스트로 만든다
sentence = "김밥,라면,돈가스"
heaven = sentence.split(",")
print(heaven)  # 출력: ['김밥', '라면', '돈가스']  → 리스트로 변환

# .replace() - 문자열.replace(찾을값, 바꿀값)

# f-string — 변수를 문자열 안에 끼워넣기
user_name = "미미"
question = "파이썬 리스트 사용 예시"
# 실무 예시: 사용자 입력값을 넣어 AI에게 보낼 프롬프트를 자동 생성
prompt = f"{user_name}님이 '{question}'에 대해 질문했습니다."
print(prompt)
# 미미님이 '파이썬 리스트 사용 예시'에 대해 질문했습니다.

# 리스트
# len() - 글자 수 세기
menu = ["김밥", "라면", "돈가스"]
print(len(menu))  # 출력: 3

# .append()

# sorted() / .sort() - 정렬 함수, sorted(리스트) (새 리스트 반환) / 리스트.sort() (원본 변경)
numbers = [6, 9, 2, 1]
print(numbers)
numbers1 = sorted(numbers)
print(numbers1)
# 출력: [1, 2, 6, 9]  (원본 numbers는 그대로)

numbers.sort()
print(numbers)  # 출력: [1, 2, 6, 9]  (원본 자체가 바뀜)

# 슬라이싱 [시작:끝]

# .index() / in - 원하는 값 찾기, 값 in 리스트 (있는지 확인), 리스트.index(값) (몇 번째인지 확인)
fruits = ["apple", "melon", "grape"]
print("apple" in fruits)      # 출력: True
print(fruits.index("melon"))  # 출력: 1  (0번부터 세서 두 번째)

# 리스트 컴프리헨션(List Comprehension) — 반복문을 한 줄로, [표현식 for 항목 in 리스트 if 조건]
ai_comments = ["네", "안녕하세요! 무엇을 도와드릴까요?", "좋아요", "잘 모르겠습니다"]

long_comments = [text for text in ai_comments if len(text) >= 12]

print(long_comments)
# ['안녕하세요! 무엇을 도와드릴까요?'] 길이가 12 이상인 것만 필터링하여 가져온다.

# 딕셔너리
# .get() - 에러 없이 vaule를 가져올 수 있다, 딕셔너리[key] 또는 딕셔너리.get(key)
student = {"name": "미미", "job": "AI서비스개발자"}
print(student["name"])          # 출력: 미미
print(student.get("age"))       # 출력: None (에러 없이 안전하게 처리, "age" 서랍이 없음)
print(student.get("age", 20))   # 출력: 20 (없을 때 기본값 지정 가능)
print(student) # age가 추가되진 않음

# .keys() - 딕셔너리.key(), 모든 키 값 확인하기
student = {"name": "미미", "job": "AI서비스개발자"}
print(student.keys())
# 출력: dict_keys(['name', 'job'])

# .values() - 딕셔너리.values(), 모든 value 값 확인하기
print(student.values())
# 출력: dict_values(['name', 'job'])

# .items() - for key, value in 딕셔너리.items():    - key와 value를 짝을 지어 순회하기
profile = {"이름": "미미", "취미": "개발"}
for key, value in profile.items():    
    print(f"{key} : {value}")   
# 이름 : 미미 
# 취미 : 개발

# .update() - 딕셔너리.update({key : value})   - 기존 내용을 수정하거나 추가하기
profile = {"이름": "미미", "취미": "개발"}
profile.update({"취미": "게임", "나이": 20})
print(profile)
# {'이름': '미미', '취미': '게임', '나이': 20}

# 중첩 딕셔너리(Nested Dictionary) 다루기 - AI API가 돌려주는 JSON 응답이 보통 중첩 구조
# 딕셔너리["key1"]["key2"]
response = {    
            "id": "fseraf-1012u12",   
            "choices": [ 
                { "message": { "role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"  } } 
                ]
            } 
# 딕셔너리 안 리스트, 리스트 안 딕셔너리를 순서대로 열어 답변만 꺼낸다.
answer = response["choices"][0]["message"]["content"]
print(answer)  # 안녕하세요! 무엇을 도와드릴까요?

print()

# 소문자 대문자 바꾸기
word = "Learn Python"
result = ""
for i in word:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i
print(result) # lEARN pYTHON

print()

# 두 딕셔너리 병합하기
# menu1을 기준으로 menu2의 내용을 합쳐 - (겹치는 키 "샌드위치"는 menu2의 값으로 덮어써서) 
# 하나의 딕셔너리로 만들고, 그 결과를 items()로 반복하며 "메뉴명: 가격" 형태로 한 줄씩 출력하세요
menu1 = {"커피": 7000, "샌드위치": 9500}
menu2 = {"샌드위치": 8000, "쿠키": 4000}
menu1.update(menu2)

for name,price in menu1.items():
    print(f"새로 바뀐 메뉴 {name}:{price}")
print()
print(menu1) # 샌드위치 값이 변함
print()
print(menu2)

print()

# 단어별 등장 횟수 세기 (빈도수 계산하기)
# text를 단어 단위로 나눈 뒤, 각 단어가 몇 번씩 등장하는지 딕셔너리 형태로 만들어 출력하세요.
text = "cherry apple banana apple cherry banana apple apple banana"

# 1. count 딕셔너리 생성
count = {}
# 2. 공백을 기준으로 words 리스트 생성
words = text.split()
# 3. 단어별 횟수를 셈
for fruits in words:
    if fruits in count:
        count[fruits] = count[fruits] + 1
    else:
        count[fruits] = 1

# 4. count 딕셔너리 출력
print(count)  # {'cherry': 2, 'apple': 4, 'banana': 3}