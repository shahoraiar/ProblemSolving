# problem : https://codeforces.com/problemset/problem/110/A

number = input()

count = 0
for n in number:
    if n == '4' or n == '7':
        count += 1

final = 0
for c in str(count):
    if c == '4' or c == '7':
        final += 1

if len(str(count)) == final:
    print("YES")
else:
    print("NO")


