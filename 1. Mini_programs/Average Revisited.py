# n = 0
# list_1 = []
# while n <= 4:
#     num = int(input('Enter the number: '))
#     list_1.append(num)
#     n += 1
# tot_1 = len(list_1)

# sum_1 = sum(list_1) 
# avg = sum_1/tot_1
# print(avg)

##############################################

n = 0
list_1 = []
while True:
    try:
        num = int(input('Enter the number: '))
        list_1.append(num)
        n += 1
    except ValueError:
        print('***** Empty input, Programe executed *****')
        break
tot_1 = len(list_1)
sum_1 = sum(list_1) 
avg = sum_1/tot_1
print(f"The total no. of inputs: {tot_1}, sum of the inputs: {sum_1}\nThe average is: {avg}") 

##############################################

n = 0
list_1 = []
while num := int(input('Enter the number: ')):
        list_1.append(num)
        n += 1
tot_1 = len(list_1)
sum_1 = sum(list_1) 
avg = sum_1/tot_1
print(f"The total no. of inputs: {tot_1}, sum of the inputs: {sum_1}\nThe average is: {avg}") 