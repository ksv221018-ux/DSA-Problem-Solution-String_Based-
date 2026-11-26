text=input("Enter the text:")
arr=list(text)
n=len(arr)

left=0
right=n-1

while left < right:
    if arr[left]=='a' or arr[left]=='e' or arr[left]=='i' or arr[left]=='o' or arr[left]=='u':
        left=left+1
    elif arr[right]=='a' or arr[right]=='e' or arr[right]=='i' or arr[right]=='o' or arr[right]=='u':
        right=right-1
    else:
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left=left+1
        right=right-1
print("".join(arr))