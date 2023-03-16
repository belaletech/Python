"""
          **for loop**
--------------------------------
1.for loop is used for sequential traversal.
it can be used to traverse string or array.
3.Iterating over a sequence is called traversal.
4.For loop is used to iterate over a sequence (list,string,tuple etc).
----------------------------------

      **Syntax**
  for variable in sequence:
      body of for_loop
-----------------------------------

1.Range(1,6,2)
#start=1
#contion<6
#increament=2



2.Range(6)
#start=0
#contion<6
#increament=1


3.Range(1,5)
#start=0
#contion<5
#increament=1




WAP TO TABLE OF NUMBER THROUGH USERINPUT

"""


"""for x in range(5):
    print("first",x)

for y in range(1,6):
    print("second",x)

for z in range(1,6,2):
    print("third",z)
    """


#WAP TO TABLE OF NUMBER THROUGH USERINPUT
"""
x=int(input("Enter your number\n"))
print('Table of ',x,"is given below")
for i in range(1,11):

    print(x*i)

#y=int(input("Enter your number for reversing\n"))
print("reversed is given below")
for y in range(10,0,-1):
    print(y)"""


#list program
l=[10,5,25,25,]
print(type(l))