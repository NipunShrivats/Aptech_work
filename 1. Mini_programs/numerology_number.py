##### NUMEROLOGY number #####
# Input 2 numbers.
# Adding the digits of each of the number eg num1 = 27 num2 = 12
# Adding --> (2+7) + (1+2) -------> 9 + 3 ---> 12
# The numerology numbers can not be greater than 9 so we have to re-perform the operation on the any number greater than 9
# After operating on number 12 ---> well get 1 + 2 --> 3, Hence 3 is the numerology number. 

###########################################################################################################

date = int(input('Enter the date: '))
month = int(input('Enter the month number: '))

temp_d = date
sum_d = 0
red_d = 0

temp_m = month
sum_m = 0
red_m = 0

while temp_d > 0:
    rem_d = temp_d % 10
    sum_d = sum_d + rem_d
    temp_d = temp_d // 10

while temp_m > 0:
    rem_m = temp_m % 10
    sum_m = sum_m + rem_m
    temp_m = temp_m // 10

sum_1 = sum_d + sum_m
if sum_1 <= 9:
    print(f"Your Numerology number is: {sum_1}")
else:
    temp_last = sum_1
    rem_last = 0
    sum_last = 0
    while temp_last > 0:
        rem_last = temp_last % 10
        sum_last = sum_last + rem_last
        temp_last = temp_last // 10
    print('\n')
    print(f"Your Numerology number is: {sum_last}") 