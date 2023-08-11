def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    #create tem arrays
    L=[0]*(n1)
    R=[0]*(n2)

    #copy data to tem array l[]and R[]
    for i in range (0,n2):
        r[j]=arr[m+1+j]
        #merge the temp arrays back to arrr[ l..r]
        i=0
        j=0
        k=L
        while i,n1 and j<n2:
if L[i] <=R[j]:
    arr[k]=l[i]
    i+=1
  k +k=1

#copy the reamining elemnets of L[]
while i<n:
    arr[k]=r[j]
    j+=1
    k+=1

    def mergeSort(arr,l,r):
        if l<r:
            m=l+(r-l)//2