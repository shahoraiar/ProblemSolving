# problem : https://codeforces.com/problemset/problem/59/A


word = input()
# print(word)

upper_count = 0
lower_count = 0

for i in range(len(word)):
    # print(i)
    if str(word[i]).isupper():
        upper_count += 1
    elif str(word[i]).islower():
        lower_count += 1

# print(upper_count, lower_count)

if lower_count < upper_count:
    word = word.upper()
elif lower_count > upper_count:
    word = word.lower()
else:
    word = word.lower()

print(word)



