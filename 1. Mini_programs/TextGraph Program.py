## TextGraph Program
## Draw a bar graph using characters printed in the console window. 
## The TextGraph program prompts the user to enter up to ten positive whole numbers no larger than 50 separated by space characters. 
## After the user hits return, the program generates a bar graph … one bar for each valid1 number entered. 
## Each bar contains a number of “=” characters equal to the one of the numbers entered.

# n = 0
# list_1 = []

# while n <= 10:
#     num = str(input('Enter the number: '))
#     list_1.append(num)
#     n += 1
# print(list_1) 
# print('\n')

n = 0
str_1 = ''
while n <= 2:
    num = str(input('Enter the number: ')) + ' ' # for spliting by 'gap'
    str_1 += num
    n += 1
    print(str_1)
str_1 = str_1.split(' ')
print('\n')

print('GRAPH: ')
for s in str_1:
    if s.isnumeric() == True:
        if int(s) < 0 or int(s) > 50:
            print(f"{s}: ?")
        else: 
            val = int(s) * '='
            print(f"{s}: {val}")
    elif s.isalpha() == True:
        print(f"{s}: ?")
    else:
        print('This method is not found in the directory')
