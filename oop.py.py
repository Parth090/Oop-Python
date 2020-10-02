'''l1 = [89,"python",98,67,"hello"]
num = []
chaa = []
for i in l1:
    if type(i) == int:
        num.append(i)
    else:
        chaa.append(i)
print(num)
print(chaa)'''

'''
num = input("Enter number scored by aditya : ")
if num.isdigit():
    num = int(num)
    if num < 50 and num >=30:
        print("Aditya scored %d %% which is third division"%(num))
    elif num < 60 and num > 50:
        print("Aditya scored %d %% which is second divison"%(num))
    elif num >= 60:
        print("Aditya scored %d %% which is first division"%(num))
    else:
        print("Aditya is failed")
else:
    print("Invalid input")'''


'''
num = int(input("Enter number :"))
b = []
for i in range(1,num+1):
    b.append(i)
print(b) '''    


'''
def addnums(num1,num2):
    num3 = num1 + num2
    print(num3)


addnums(3,5)'''

# def category():
#     '''Chose a category
#     1.Arthmatic
#     2.logical'''
#     cat = int(input("Enter category :"))
#     if cat == 1:
#         print(arth.__doc__)
#         arth()
#     elif cat == 2:
#         logical()
#     else:
#         print("Invalid input..")

# def arth():
#     '''chose operation
#     1.Add
#     2.Sub
#     3.Div '''
#     ope = int(input("Enter operation : "))
#     num1 = int(input("Enter number :"))
#     num2 = int(input("Enter second number :"))

#     if ope == 1:
#         num3 = addnums(num1,num2)
#         print(num3)
#     elif ope == 2:
#         num3 = addsubr(num1,num2)
#         print(num3)
#     elif ope == 3:
#         num3 = adddiv(num1,num2)
#         print(num3)
#     else:
#         print("Invalid input : ")
# def addnums(num1,num2):
#     res = num1 + num2
#     return res
# def addsubr(num1,num2):
#     res = num1 - num2
#     return res
# def adddiv(num1,num2):
#     res = num1/num2
#     return res

# print(category.__doc__)
# category()

# print("c:\\programs\\files\\new\\code\\test")

# message = "hello world"
# print(message)
# greetings = "welcome"

# new_msg = '{},{}  hii how are !!!'.format(message,greetings)
# new_1 = f'{message},{greetings.upper()}'
# print(new_msg)
# print(new_1)

# new_2 = "old"
# new_message = message.replace('world',new_2)
# print(new_message)
# print(dir(message))
# print(help(str))


strings = 'aditya'
l = []

for i in range(-1,-len(strings)-1,-1):
    print(strings[i],end="")