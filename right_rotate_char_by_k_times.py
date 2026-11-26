text=input("Enter the text:")
arr=list(text)
n=len(arr)

k=int(input("Enter the K:"))
k=k%n

i=0
j=n-1

while i < j:
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i=i+1
    j=j-1

a=0
b=k-1

while a < j:
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    a=a+1
    b=b-1

c=k
d=n-1

while c < d:
    temp=arr[c]
    arr[c]=arr[d]
    arr[d]=temp
    c=c+1
    d=d-1

for i in range(0,n):
    print(arr[i],end="")