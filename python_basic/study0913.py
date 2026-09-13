# 문제 풀이

# 그림확대 문제
'''
## 문제 요약

문자열 배열로 표현된 그림과 확대 배율 `k`가 주어진다.

각 픽셀을 가로와 세로 방향으로 `k`배씩 늘려서 새로운 그림을 만들어 반환한다.

즉, 한 문자는 가로로 `k`번 반복하고, 만들어진 한 줄은 세로로 `k`번 반복한다.

## 풀이 핵심

각 문자열의 문자를 하나씩 확인하면서 `k`번 반복해 새로운 한 줄을 만든다.

완성된 한 줄을 다시 `k`번 추가하면 세로 방향 확대까지 처리할 수 있다.
'''
def solution(picture, k):
    answer = []
    for i in picture:
        row = ""
        for j in i:
            row += j * k # 문자 하나하나를 k번 반복
        
        for j in range(k):
            answer.append(row) # 반복한 row를 k번 추가해서 세로를 늘리는 것
    return answer
# picture의 한줄
# 문자 하나씩 k배 -> 가로확대
# 완성된 한줄을 k번 추가 -> 세로 확대

def solution(picture, k):

    answer = []

    for i in range(len(picture)):
        answer += [picture[i].replace('.', '.'*k).replace('x', 'x'*k)] * k

    return answer

# replace() 를 사용해서 풀 수도 있다

print()

# 특별한 이차원 배열
'''
## 문제 요약

정수 `n`이 주어졌을 때 `n x n` 크기의 2차원 배열을 만든다.

행과 열의 번호가 같은 위치, 즉 `i == j`인 곳에는 `1`을 넣고 나머지 위치에는 `0`을 넣는다.

결과적으로 왼쪽 위에서 오른쪽 아래로 이어지는 대각선에만 `1`이 들어간 배열을 만든다.

## 풀이 핵심

이중 반복문을 사용해 모든 행과 열의 위치를 확인한다.

현재 행 번호와 열 번호가 같으면 `1`, 다르면 `0`을 추가한다.
'''
def solution(n):
    answer = []  # 최종적으로 n x n 행렬을 담을 리스트

    for i in range(n):  # 행(row)을 하나씩 만든다
        row = []  
        for j in range(n):  # 현재 행에서 열을 하나씩 확인한다.
            if i == j:
                row.append(1)
            else:
                row.append(0)
        answer.append(row)

    return answer

print()

# 정수를 나선형으로 배치하기
'''
## 문제 요약

정수 `n`을 기준으로 `n × n` 크기의 배열을 만든다.

1부터 `n²`까지의 숫자를 배열의 왼쪽 위에서 시작해 시계 방향으로 나선형이 되도록 차례대로 배치한다.

## 풀이 핵심

배열의 위쪽, 아래쪽, 왼쪽, 오른쪽 경계를 정해놓고 바깥쪽부터 한 바퀴씩 숫자를 채운다.

한 바퀴를 완성할 때마다 사용한 행과 열의 범위를 안쪽으로 좁혀가면서 반복한다.
'''

# 보통 i = 행, j = 열

def solution(n):
    # n x n 크기의 0으로 채워진 2차원 배열 만들기
    answer = [[0] * n for _ in range(n)] # _는 반복 횟수 변수는 필요 없으니 그냥 n번 반복해!라는 뜻

    # 현재 넣을 숫자
    num = 1

    # 위쪽, 아래쪽, 왼쪽, 오른쪽의 경계
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    # 숫자를 다 채울 때까지 반복
    while top <= bottom and left <= right:

        # 1. 왼쪽 → 오른쪽
        for j in range(left, right + 1):
            answer[top][j] = num
            num += 1
        top += 1

        # 2. 위쪽 → 아래쪽
        for i in range(top, bottom + 1):
            answer[i][right] = num
            num += 1
        right -= 1

        # 3. 오른쪽 → 왼쪽
        for j in range(right, left - 1, -1):
            answer[bottom][j] = num
            num += 1
        bottom -= 1

        # 4. 아래쪽 → 위쪽
        for i in range(bottom, top - 1, -1):
            answer[i][left] = num
            num += 1
        left += 1

    return answer

print()

# 정사각형으로 만들기
'''
## 문제 요약

2차원 배열의 행과 열의 개수를 비교해서 정사각형 형태로 만든다.

행이 열보다 많다면 각 행의 끝에 `0`을 추가한다.

반대로 열이 행보다 많다면 부족한 만큼 `0`으로 이루어진 행을 추가한다.

## 풀이 핵심

먼저 행의 개수와 열의 개수를 구한 뒤 두 값을 비교한다.

행이 더 많으면 각 행에 필요한 만큼 `0`을 추가하고, 열이 더 많으면 필요한 개수만큼 `[0]`으로 이루어진 행을 추가한다.

'''

def solution(arr):
    row = len(arr) # arr의 행(row) 개수를 구한다.
    col = len(arr[0]) # arr의 열(column) 개수를 구한다.

    if row > col:
        for i in arr:  # arr의 각 행을 하나씩 꺼낸다. i는 [1, 2] 같은 '한 줄' 자체가 된다.
            for j in range(row - col):
                i.append(0)
    elif col > row:
        for i in range(col - row):
            arr.append([0] * col)
    return arr

print()

# 이차원 배열 대각선 순회하기
'''
## 문제 요약

2차원 배열 `board`와 정수 `k`가 주어진다.

각 원소의 행 번호를 `i`, 열 번호를 `j`라고 할 때 `i + j <= k`를 만족하는 위치의 값만 골라 모두 더한다.

## 풀이 핵심

이중 반복문으로 배열의 모든 위치를 확인한다.

각 위치에서 `i + j <= k` 조건을 확인하고, 조건을 만족하면 해당 위치의 값을 `answer`에 더한다.
'''

def solution(board, k):
    answer = 0

    # 행을 하나씩 확인, i는 현재 행의 번호
    for i in range(len(board)):

        # 현재 행에서 열을 하나씩 확인, j는 현재 열의 번호
        for j in range(len(board[i])):

            if i + j <= k:

                # 현재 위치의 값을 answer에 더한다. board[i][j] = i번째 행, j번째 열의 값
                answer += board[i][j]

    return answer