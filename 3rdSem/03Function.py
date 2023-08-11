def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return (a,b)
c=int(input("Enter Your first number : "))
d=int(input("Enter your second number : "))
c,d = swap(c,d)
print(c,d)
