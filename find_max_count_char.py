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
    if freq[i] > -1:
        freq[i]=count

maximum=float('-inf')
max_char=""

for i in range(0,n):
    if freq[i] > maximum:
        maximum=freq[i]
        max_char=arr[i]

print("Maximum char:",max_char)
print("maximum frequency:",maximum)
        

