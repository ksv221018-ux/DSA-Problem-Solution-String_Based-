text=input("Enter the text:")
arr=list(text)
n=len(arr)

temp=arr[n-1]

for i in range(n-1,0,-1):
    arr[i]=arr[i-1]

arr[0]=temp

for i in range(0,n):
    print(arr[i],end="")
    