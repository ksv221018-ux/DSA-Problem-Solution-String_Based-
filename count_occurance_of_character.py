text=input("Enter the Text:")
arr=list(text)
n=len(arr)

target=input("Enter the ch to count:")
count=0

for i in range(0,n):
    if arr[i]==target:
        count=count+1

print("Occurance of the Character:",count)
