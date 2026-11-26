text=input("Enter the Text:")
arr=list(text)
n=len(arr)

for i in range(0,n):
    if arr[i]>='A'and arr[i]<='Z':
        arr[i]=chr(ord(arr[i])+32)
    elif arr[i]>='a' and arr[i] <='z':
        arr[i]=chr(ord(arr[i])-32)

print("".join(arr))