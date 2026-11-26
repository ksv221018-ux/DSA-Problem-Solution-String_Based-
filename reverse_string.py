text=input("Enter Text:")
arr=list(text)
n=len(arr)

start=0
end=n-1

while start < end:
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start=start+1
    end=end-1

print("".join(arr))