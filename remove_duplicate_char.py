text=input("Enter the Text:")
arr=list(text)
n=len(arr)
result=[]

for i in range(0,n):
    if arr[i] not in result:
        result.append(arr[i])
print("".join(result))