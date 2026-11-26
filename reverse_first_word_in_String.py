text=input("Enter the Text:")
arr=text.split(" ")
n=len(arr)

result=""

for i in range(0,n):
    word=arr[i]
    charr=list(word)
    m=len(charr)

    start=0
    end=m-1

    if i==0:
        while start < end:
            temp=charr[start]
            charr[start]=charr[end]
            charr[end]=temp
            start=start+1
            end=end-1
        
        result=result+"".join(charr)+" "
    else:
        result=result+word+" "

print(result)