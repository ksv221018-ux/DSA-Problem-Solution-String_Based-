text=input("Enter the Sentence:")
arr=text.split(" ")
n=len(arr)

k=int(input("Enter the K:"))

for i in range(0,k):
    print(arr[i],end=" ")