text=input("Enter the Text:")
arr=text.split(" ")
n=len(arr)

start=0
end=n-1

while start < end:
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start=start+1
    end=end-1

print(" ".join(arr))