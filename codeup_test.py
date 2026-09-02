n = int(input()) # n번 무작위로 부른 횟수
a = input().split # n번만큼 부른 출석 번호

for i in range(n):
	a[i] = int(a[i])

b = []
for i in range(24):
	b.append(0)

for i in range(n):
	b[a[i]] += 1

for i in range(1, 24):
	print(b[i], end = ' ')