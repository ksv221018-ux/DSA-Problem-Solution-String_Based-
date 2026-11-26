text=input("Enter the Sentence:")
arr=text.split(" ")
k=int(input("Enter the K:"))

left=0
right=k-1

while left < right:
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp

    left=left+1
    right=right-1

print(" ".join(arr))