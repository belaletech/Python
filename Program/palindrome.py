no=int(input("Enter your number\n"))
cpy=no
rev=0
while no!=0:
    #extracting last digit
    r=no%10;
    rev=rev*10+r
    #remove last digit
    no=int(no/10)
if cpy==rev:
      print("Given number is palindrome")
else:
     print("Not Palindrome")
