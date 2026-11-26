text=input("Enter the text:")
arr=list(text)
n=len(arr)

freq=[0]*n

for i in range(0,n):
    count=1
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            count=count+1
            freq[j]=-1
    if freq[i]>-1:
        freq[i]=count

for i in range(0,n):
    if freq[i]==1:
        print(arr[i])