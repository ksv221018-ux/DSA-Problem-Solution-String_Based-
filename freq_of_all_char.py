text=input("Enter the text:")
arr=list(text)

freq={}

for i in range(0,len(arr)):
    if arr[i] in freq:
        freq[arr[i]]=freq[arr[i]]+1
    else:
        freq[arr[i]]=1

print(freq)