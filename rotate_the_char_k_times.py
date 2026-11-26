text=input("Enter the Text:")
arr=list(text)
n=len(arr)

k=int(input("Enter the K:"))
k=k%n

i=0
j=k-1

while i < j:
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i=i+1
    j-j-1

a=k
b=n-1

while a < b:
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    a=a+1
    b=b-1

start=0
end=n-1

while start < end:
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start=start+1
    end=end-1

for i in range(0,n):
    print(arr[i],end="")