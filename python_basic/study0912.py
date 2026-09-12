# 문제풀이

# 조건에 맞게 수열 변환하기 2
'''
정수 배열 arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

이런 작업을 n번 반복한 결과인 배열을 arr(n)라고 표현한다면
arr(n) = arr(n + 1)인 n이 항상 존재합니다. <-- 완전히 동일한 배열이 생긴다는 뜻
이런 일이 발생할 때의 n 값을 return 하는 solution 함수를 완성해 주세요.

단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 서로 같음을 의미합니다.

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