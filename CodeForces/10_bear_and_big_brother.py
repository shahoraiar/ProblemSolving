# problem : https://codeforces.com/problemset/problem/791/A

weight = input().split()

a = int(weight[0])
b = int(weight[1])

for i in range(12):
    i += 1
    # print(i)
    a = a * 3
    b = b * 2
    # print(i, a, b)
    if a > b:
        print(i)
        break
