# 문제풀이

# 조건에 맞게 수열 변환하기 2
'''
## 문제 요약

배열의 각 숫자를 특정 조건에 따라 반복해서 변경한다.

- 50 이상이면서 짝수인 값 → 2로 나눈다.
- 50 미만이면서 홀수인 값 → 2를 곱한 뒤 1을 더한다.
- 위 조건에 해당하지 않는 값은 그대로 둔다.

이 변환을 계속 반복했을 때 어느 순간부터 배열의 상태가 더 이상 변하지 않는다.

배열이 처음으로 이전 상태와 동일해지는 시점의 반복 횟수를 구한다.
'''
def solution(arr):
    count = 0
    while True:
        new_arr = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                new_arr.append(num // 2)
            elif num < 50 and num % 2 == 1:
                new_arr.append(num * 2 + 1)
            else:
                new_arr.append(num)
        if new_arr == arr:
            return count
        
        arr = new_arr
        count += 1

print()

# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
'''
## 문제 요약

문자열 `myString`과 특정 문자열 `pat`이 주어진다.

`myString` 안에서 `pat`으로 끝나는 부분 문자열 중 가장 긴 것을 찾아 반환한다.
'''
def solution(myString, pat): 
    return myString[:myString.rfind(pat) + len(pat)]
# rfind() - 마지막으로 등장하는 위치를 알려준다
# myString = "dddddddaa"
# myString.rfind("a") # 8

print()

# 배열 만들기
'''
## 문제 요약

0과 1로 이루어진 배열을 왼쪽부터 하나씩 확인하면서 새로운 스택 형태의 배열을 만든다.

현재 값을 스택에 넣을 때 다음 규칙을 적용한다.

- 스택이 비어 있으면 현재 값을 추가한다.
- 스택의 마지막 값과 현재 값이 같으면 마지막 값을 제거한다.
- 두 값이 다르면 현재 값을 스택의 마지막에 추가한다.

모든 원소를 확인한 뒤 만들어진 배열을 반환한다.

단, 최종 결과가 빈 배열이라면 `[-1]`을 반환한다.
'''

def solution(arr):
    stk = []

    for i in arr:
        if stk and stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)

    if not stk:
        return [-1]

    return stk

print()

# 문자열 묶기
'''
## 문제 요약

문자열 배열에 들어 있는 문자열들을 문자열의 길이를 기준으로 분류한다.

예를 들어 길이가 3인 문자열끼리 하나의 그룹, 길이가 5인 문자열끼리 또 하나의 그룹으로 묶는다.

이렇게 만들어진 여러 그룹 중에서 **원소가 가장 많이 들어 있는 그룹의 크기**를 반환한다.
'''
def solution(arrStr):
    count = {}
    for i in arrStr:
        length = len(i)
        if length not in count:
            count[length] = 1
        else:
            count[length] += 1
    return max(count.values()) # [2,2,1] 중에 가장 큰 값

print()

