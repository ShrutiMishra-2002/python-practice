print("multiplication table")
#int is used for making it addition, otherwise it prints
#3,33,333 
num = int(input("enter no:"))
for i in range(1, 11):
    print(num , 'x', i, '=', num * i)
#'' is used for print * and = 