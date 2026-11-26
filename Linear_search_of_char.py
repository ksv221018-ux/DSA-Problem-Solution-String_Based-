text=input("Enter the text:")
arr=list(text)
n=len(arr)

target=input("Enter the char:")
status=False

for i in range(0,n):
    if arr[i]==target:
        status=True
        print("char Founded at index,",i)
        break

if status==False:
    print("Element not Founded not in the list")
