""""if Statement
    if[conditional Expression]:
      [statement(s) to execute]
      [           ]
      [           ] 

      1.write a program to print first 10 natural number.
      
      2.Write a program to print first 10 even number.
      3.Write a program to print first 10 odd number.
      4.Write a program to print first 10 even numbers in reverse order.
      4.write a program to print table of number accepted by user.
      5.write a program to print product of a digit a number.
      6.write a program to print find a factorial of a number.
      """""

a=int(input("Enter your no\n"))
if(a%2==0):
    print(a," is even number")
else:
    print(a," is Odd")

#1.write a program to print first 10 natural number.

print("====The First 10 Natural Numbers====")

for i in range(1, 11):
    print(i)
#2.Write a program to print first 10 even number.
print("====The First 10 Even Natural Numbers====")

for i in range(1, 11):
    print(2 * i)

#Write a program to print first 10 odd number.
print("====The First 10 Odd Natural Numbers====")

for i in range(1, 11):
    print(2 * i - 1)

#Write a program to print first 10 even numbers in reverse order
for i in range(20, 0, -2):
    print(i)
    if i == 2:
        break
#write a program to print find a factorial of a number
num = int(input("Enter a number: "))

factorial = 1

# if the input number is negative, print an error message
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
    
# if the input number is 0 or 1, the factorial is 1
elif num == 0 or num == 1:
    print("The factorial of", num, "is 1")
    
# for any other number, calculate the factorial using a loop
else:
    for i in range(2, num+1):
        factorial *= i
    print("The factorial of", num, "is", factorial)



