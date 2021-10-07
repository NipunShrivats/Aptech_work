## find if given number is an ARMSTRONG NUMBER or not ##

# num = int(input('Enter the number: '))
# org = num
# sum = 0

# while (org > 0): # the loop will terminate when num = or less than 0
#     rem = org % 10 # quotient
#     sum = sum + (rem ** 3)
#     org = org // 10 # remainder

# if num == sum:
#     print(f"{num} number is a armstrong nummber.")
# else:
#     print(f"{num} is not a armstrong number.")

####################################################################

## print armstrong number between given intervals.##

# lower = int(input('Enter the lower number: '))
# upper = int(input('Enter the upper number: '))

# for num in range(lower, upper+1):
#     sum = 0
#     org = num
#     while org > 0:
#         rem = org % 10
#         sum = sum + (rem ** 3)
#         org = org // 10
#         if num == sum:
#             print(num)

####################################################################

## find PALINDROME numbers. - eg = 121, 323 (ulta-sidha same).

# num = int(input('Enter the number: '))
# temp = num
# rev = 0 # reverse

# while temp > 0:
#     digg = temp % 10
#     rev = rev * 10 + digg
#     temp = temp // 10
# if num == rev:
#     print("TRUE")
# else: 
#     print('FALSE')

####################################################################

## Strong Number --> sum of each number's factorial = the same number ##
# eg - 145 
# 1! = 1
# 4! = 24
# 5! = 120
# 120 + 24 + 1 = 145

# num = int(input("Enter the number: "))
# temp = num
# fact = 0
# while temp > 0:
#     f = 1
#     rem = temp % 10
#     for r in range(1, rem+1):
#         f = f * r
#     fact = fact + f
#     temp = temp // 10

# if fact == num:
#     print(f"{num} is a strong number")
# else:
#     print(f"{num} is not a strong number")
