a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
d = int(input("Enter the fourth number : "))

tup1 = a,b
tup2 = c,d
print(tup1 , tup2)

temp_var1 = int(''.join(map(str, tup1)))
temp_var2 = int(''.join(map(str, tup2)))
print(temp_var1 , temp_var2)

if d == (2 * a):
    if b == c :
        if temp_var1 + temp_var1 == temp_var2:
            print("You entered the correct magic number: ", a,b,c,d)
        else:
            print("This is not the correct magic number. Please try again..!!")
    else:
            print("Second number is not same as third number")
else:
            print("Fourth number is not double of first number")
