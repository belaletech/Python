a=int(input("Enter any number = "))
s=0
m=a
while(a!=0):
    r=a%10
    s=s*10+r
    a=a//10
if(s==m):
    print("Number is palindrome")
else:
    print("number is not palindrome")