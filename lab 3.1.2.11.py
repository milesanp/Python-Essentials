wordWithoutVovels = ""
userWord = input("Please enter your word:")
userWord = userWord.upper()

for wordWithoutVovels in userWord:
    if wordWithoutVovels == "A":
        continue
    elif wordWithoutVovels == "E" :
        continue
    elif wordWithoutVovels == "I" :
        continue
    elif wordWithoutVovels == "O" :
        continue
    elif wordWithoutVovels == "U" :
        continue
    else :
        print(wordWithoutVovels, end ="")
