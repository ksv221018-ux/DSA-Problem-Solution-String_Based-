text=input("Enter the Text:")
arr=list(text)
n=len(arr)

status=True

start=0
end=n-1

while start < end:
    if arr[start]!=arr[end]:
        status=False
        break
    start=start+1
    end=end-1

if status==True:
    print("Palindrome")
else:
    print("Not Palindrome")