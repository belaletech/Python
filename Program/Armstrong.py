no=int(input("Enter any number to find number is Armstrong or Not\n"))
cpy=no
sum=0
while no!=0:
    r=no%10;
    sum=sum+(r*r*r)
    no=int(no/10)
if cpy==sum:
    print("Given number is Armstrong")
else:
    print("Not Armstrong")