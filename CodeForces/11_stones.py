# problem : https://codeforces.com/problemset/problem/266/A

s_number = int(input())
color = list(input())

# print(color, len(color))
count = 0

for i in range(s_number):
    # print(i)
    if (i+1) == len(color): break
    if color[i] == color[i+1] : 
        count += 1

    # print(color, len(color))

print(count)

