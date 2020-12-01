N = int(input())
total = 0
for i in range(N):
    q1 = input().split()
    num = float(q1[0])
    num1 = float(q1[1])
    total += num1 * num

round(total , 4)
print(total)
