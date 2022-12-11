a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
d = float(input("Enter 4th number: "))
e = float(input("Enter 5th number: "))
if((a <= 0) or (b<=0) or (c<=0) or (d<=0) or (e<=0)):
    print("Entered numbers having values less than or equal to 0, Please enter Positive number !!!")
else:
    print("Entered 1st number: ",a)
    print("Entered 2nd number: ",b)
    print("Entered 3rd number: ",c)
    print("Entered 4th number: ",d)
    print("Entered 5th number: ",e)
    print("Total: ",a+b+c+d+e)