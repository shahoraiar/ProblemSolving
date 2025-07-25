value = input().split()

first_pc_price = int(value[0])
total_dollar = int(value[1])
banana = int(value[2])

sum = 0
for i in range(banana):
    i = i + 1
    # print(i)
    # print('per_pc_price : ', first_pc_price, '*', i)
    sum = sum + (first_pc_price * i)
    # print('sum : ', sum)

# print('total price : ', sum)

return_dollar = sum - total_dollar

if return_dollar < 0:
    print(0)
else:
    print(return_dollar)


