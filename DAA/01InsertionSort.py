# insertion sort in python

def insertionSort(array):
  for i in range(1,len(array)):
    temp=array[i]
    j=i-1

    while j>=0 and temp<array[j]:
      array[j+1]=array[j]
      j=j-1
      array[j+1]=temp
#array=[10,5,25,18]
array=[]
numElement=int(input("Enter the number of elements: "))

for i in range(numElement):
  element=int(input("Enter {}:".format(i+1)))
  array.append(element)
insertionSort(array)
print("Sorting array",array)