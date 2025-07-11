sentence=input("Enter the sentence:")
words=sentence.split()
un_words=[]
fr=[]
for w in words:
    if w in un_words:
     index=un_words.index(w)
     fr[index] +=1
else:
    un_words.append(w)
    fr.append(1)
for i in range(len(un_words)):
    print(f"{un_words[i]}:{fr[i]}")