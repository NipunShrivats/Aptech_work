# penny - 'p'
# nickel - 'n'
# dimes, quarters, half-dollars all work the same way

# Coin values are: penny = $0.01, nickel= $0.05, dime= $0.10, quarter= $0.25 and half-dollar= $0.50

# n = 0
# list_1 = []
# while n <= 4: # 17
#     num = float(input('Enter the values: '))
#     if num == 0.01:
#         list_1.append('p') # pennny
#     elif num == 0.05:
#         list_1.append('n') # nickel
#     elif num == 0.10:
#         list_1.append('d') # dime
#     elif num == 0.25:
#         list_1.append('q') # quarter
#     elif num == 0.50:
#         list_1.append('hd') # half-dollar
#     else:
#         print('Please try again: ')
#         continue
#     n += 1
# print('Enter coin list:', list_1)

n = 0
str_1 = ''
while n <= 2:
    inp = input('Enter the string value\np for penny\nn for nuckel\nd for dime\nq for quarter\nhd for half quarter : ')
    print('\n')
    str_1 += inp
    n += 1

print(str_1)
str_1 = str_1.split(' ')
print(str_1)

print('========================================================')
print('\t\tCoin Counter Report')
print('========================================================')
print('coin\t\tValue\tNumber\tAmount')
print('====\t\t=====\t =====\t =====')


# list_1 = ['p', 'q', 'hd', 'd', 'q', 'p', 'p', 'n']
# sum = 0


num_p = 0
num_n = 0
num_d = 0
num_q = 0
num_hd = 0

sum_p = 0
sum_n = 0
sum_d = 0
sum_q = 0
sum_hd = 0

for s in str_1:
    if s == 'p':
        # sum += 0.01
        num_p += 1
        sum_p += 0.01

    elif s == 'n':
        # sum += 0.05
        num_n += 1
        sum_n += 0.05

    elif s == 'd':
        # sum += 0.10
        num_d += 1
        sum_d += 0.10

    elif s == 'q':
        # sum += 0.25
        num_q += 1
        sum_q += 0.25

    elif s == 'hd':
        # sum += 0.50
        num_hd += 1
        sum_hd += 0.50
    else:
        print("Method not applicable")
# print("sum: ", sum)
tot = sum_p + sum_n + sum_d + sum_q + sum_hd

print(f"Pennies   \t$0.01\t   {num_p}\t ${sum_p}")
print(f"Nickles   \t$0.05\t   {num_n}\t ${sum_n}")
print(f"Dimes   \t$0.10\t   {num_d}\t ${sum_d}")
print(f"Quarters\t$0.25\t   {num_q}\t ${sum_q}")
print(f"Half-dollars\t$0.50\t   {num_hd}\t ${sum_hd}")
print(f"\t\tTotal Amount :   ${tot}")
print('\n')




