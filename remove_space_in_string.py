text=input("Enter the Text:")
arr=list(text)
n=len(arr)

result=""

for i in range(0,n):
    if arr[i]!=" ":
        result=result+arr[i]

print("".join(result))