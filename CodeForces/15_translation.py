# problem : https://codeforces.com/problemset/problem/41/A

word = input()
r_word = input()

w_reverse = word[::-1]

if r_word != w_reverse:
    print('NO')
else:
    print('YES')

