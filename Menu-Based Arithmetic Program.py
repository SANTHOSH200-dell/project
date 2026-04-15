print("hello")
a = int(input("enter a value1:"))
b = int(input("enter a value2:"))
print("/n choose the choices")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
choice = int(input("enter your choice:"))
if choice == 1:
    print("the sum is:", a + b)
elif choice == 2:
    print("the difference is:", a - b)
elif choice == 3:
    print("the product is:", a * b)
elif choice == 4:
    if b != 0:
        print("the quotient is:", a / b)
    else:
        print("division by zero is not allowed")    
else:    print("invalid choice")
