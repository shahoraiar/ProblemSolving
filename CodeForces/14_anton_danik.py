# problem : https://codeforces.com/problemset/problem/734/A

num = input()
win = input()

a_count = win.count('A')
d_count = win.count('D')

if a_count > d_count:
    print('Anton')
elif d_count > a_count:
    print('Danik')
else:
    print('Friendship')

