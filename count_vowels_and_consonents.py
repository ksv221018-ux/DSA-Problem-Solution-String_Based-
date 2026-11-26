text=input("Enter the Text:")
arr=list(text)
n=len(arr)

consonent=0
vowel=0

for i in range(0,n):
    if arr[i] in "aeiouAEIOU":
        vowel=vowel+1
    elif arr[i].isalpha():
        consonent=consonent+1

print("Vowels:",vowel)
print("Consonent:",consonent)
