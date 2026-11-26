str1=input("Enter str1:")
str2=input("Enter str2:")

arr1=list(str1)
arr2=list(str2)

arr1.sort()
arr2.sort()

if arr1==arr2:
    print("Anagram")
else:
    print("Not Anagram")