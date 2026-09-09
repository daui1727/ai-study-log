# 학생 성적 관리 시스템
# 리스트 안에 딕셔너리를 쓴 이유는 학생 여러 명을 관리하면서 - 리스트
# 한 명마다 이름과 점수라는 여러 정보를 같이 저장해야하기 때문 - 딕셔너리
def get_input(prompt, value):
    try:
        return input(prompt)
    except EOFError:
        print(f"입력처리 불가 -> {value} 기본 값으로 진행합니다.")

students = [      
            {"이름": "파닥몬", "점수": 90},
            {"이름": "아구몬", "점수": 75},  
            ]

def add_student(name, score):
    students.append({"이름":name, "점수":score})

def get_average():
    if not students:
        return 0
    total = 0
    avg = 0.0
    for student in students:
        total += student["점수"]  # 전체 학생의 점수 합계
        avg = total / len(students)
    return avg

def get_top_students():   # 평균 점수 이상인 학생들만
    avg = get_average()
    return [top for top in students if top["점수"] >= avg]

add_student("팔몬", 100)
print(f"평균 점수 : {get_average():.1f}")  # 평균 점수 : 88.3  
print(f"평균 이상 학생 : {get_top_students()}")  # 평균 이상 학생 : [{'이름': '파닥몬', '점수': 90}, {'이름': '팔몬', '점수': 100}] 

print()

# 장바구니에 담긴 상품(이름, 가격, 수량)의 총 결제 금액 계산하기
cart = [
    {"상품명": "키보드", "가격": 60000, "수량": 1},      
    {"상품명": "마우스", "가격": 15000, "수량": 2}
    ]

def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["가격"] * item["수량"]
    if total >= 50000:
        total = total * 0.9
    return total

final_price = calculate_total(cart)
print(f"최종 결제 금액 : {final_price: ,.0f}원")   # 최종 결제 금액 :  81,000원

print()

# 회원 등급 필터링 시스템 - 회원 목록에서 나이/구매금액 조건에 맞는 회원만 뽑아 등급을 부여한다.
members = [
            {"이름" : "김밥", "구매금액" : 1200000},
            {"이름" : "라면", "구매금액" : 600000},
            {"이름" : "떡볶이", "구매금액" : 20000}
        ]

# 구매 금액에 따른 등급 문자열을 반환
def get_grade(amount):
    if amount >= 1000000:
        return "VIP"
    elif amount >= 500000:
        return "일반"
    else:
        return "신규"

# 회원 리스트를 순회하며, 각 딕셔너리에 등급 key 값을 추가
for member in members:
    member["등급"] = get_grade(member["구매금액"])

print(f"등급이 매겨진 회원 목록 : {members}")
#등급이 매겨진 회원 목록 : [{'이름': '김밥', '구매금액': 1200000, '등급': 'VIP'}, {'이름': '라면', '구매금액': 600000, '등급': '일반'}, {'이름': '떡볶이', '구매금액': 20000, '등급': '신규'}]

vip_members = [ m for m in members if m["등급"] == "VIP" ]

print(f"VIP 회원 리스트 : {vip_members}")
# VIP 회원 리스트 : [{'이름': '김밥', '구매금액': 1200000, '등급': 'VIP'}]

print()

# 텍스트 단어 빈도수 구하는 프로그램
text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"
# 문장을 split으로 쪼개고 {단어:횟수} 형태로 구성하여 반환
def count_word(text):
    words = text.split()
    counts = {}

    for word in words:
        # dict.get(key, 기본값) : key가 존재하면 해당 값을 리턴, 없으면 기본값 0 리턴
        counts[word] = counts.get(word,0) + 1 # counts 딕셔너리에 word가 있다면 +1, 없다면 0 리턴

    return counts

word_count = count_word(text)

# 내림차순 정렬 : 가장 많이 등장하는 단어 TOP 3
sorted_words = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
top3 = sorted_words[:3]

print(f"가장 많이 등장한 단어 TOP 3 : {top3}")
# 가장 많이 등장한 단어 TOP 3 : [('좋아요', 2), ('이', 1), ('제품', 1)]

print()

# 간단한 TO-DO 리스트 관리 프로그램
# 리스트 = 할 일 여러개를 저장 / 딕셔너리 = 할 일 하나의 정보를 저장
tasks = [] # {"할일":str, "완료":bool}

def add_task(task):
    tasks.append({"할일": task, "완료": False})

def delete_task(index):
    if 0 <= index < len(tasks): # 사용자가 입력한 번호가 실제로 존재하는 번호인가? 확인
        removed = tasks.pop(index)
        print(f"'{removed['할일']}' 삭제 완료")
    else:
        print("잘못된 번호입니다.")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["완료"] = True

def show_tasks():
    if not tasks: # tasks가 비어있다면
        print("할 일 목록이 비어 있습니다.")
        return

    for i, task in enumerate(tasks): # enumerate() - i = 0, task = {"할일": "공부하기", ...} 이런 식으로 번호와 내용을 동시에 가져오는 것
        status = "완료" if task["완료"] else "미완료"
        print(f"{i}. {task['할일']} [{status}]")

def todo_run():
    while True:

        print("\n[메뉴] 1. 추가 2.삭제 3.완료처리 4.전체조회 5.종료")
        choice = input("메뉴 번호 선택 > ")

        if choice == "1":
            name = input("할 일을 입력하세요: ")
            add_task(name)

        elif choice == "2":
            idx = input("삭제할 번호: ")
            delete_task(int(idx))

        elif choice == "3":
            idx = input("완료 처리 번호 입력> ")
            complete_task(int(idx))

        elif choice == "4":
            show_tasks()

        elif choice == "5":
            print("Todo 프로그램 종료")
            break

        else:
            print("메뉴 번호는 1-5 번 까지 입니다.")

todo_run()

print()

# 
