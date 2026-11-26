text1=input("Enter text1:")
text2=input("Enter text2:")

word=text1+text1

if len(text1)==len(text2):
    if text2 in word:
        print("Rotated")
    else:
        print("Not Rotated")
else:
    print("Not Rotated")