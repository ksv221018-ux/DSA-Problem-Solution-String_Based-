text=input("Enter the text:")
arr=text.split(" ")
n=len(arr)

longest=""

for i in range(0,n):

    word=arr[i]

    if len(word) > len(longest):
        longest=word

print(longest)