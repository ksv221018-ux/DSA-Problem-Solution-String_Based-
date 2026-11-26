text=input("Enter the text:")
n=len(text)
result=""

for i in range(0,n):
    if text[i]>='a' and text[i]<='z':
        char=text[i]
    else:
        count=int(text[i])

        for j in range(0,count):
            result=result+char
print(result)