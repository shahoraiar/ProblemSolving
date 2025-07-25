year = int(input())

while year <= 9999:
    year += 1

    if len(set(str(year))) == 4: 
        # print(a, b, c, d)
        break

print(year)

