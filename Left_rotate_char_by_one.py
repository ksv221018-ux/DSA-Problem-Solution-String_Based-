text=input("Enter the text:")
arr=list(text)
n=len(arr)

temp=arr[0]

for i in range(0,n-1):
    arr[i]=arr[i+1]

arr[n-1]=temp

for i in range(0,n):
    print(arr[i],end="")