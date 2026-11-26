sentence=input("Enter the sentence:")
arr=sentence.split(" ")
n=len(arr)

for i in range(0,n):
    if len(arr[i])%2==0:
        word=list(arr[i])
        left=0
        right=len(word)-1

        while left < right:
            temp=word[left]
            word[left]=word[right]
            word[right]=temp

            left=left+1
            right=right-1
        arr[i]="".join(word)
print(" ".join(arr))