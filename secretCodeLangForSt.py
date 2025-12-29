st = input("Enter Message :")   
words = st.split(" ")
coding = input("Enter 1 for Coding or 0 for Decoding :")
coding = True if (coding=="1") else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkm"
            stnew = r1+ word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("---Your Encoded String---")
    print(" ".join(nwords)) 

else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("---Your Decoded String---")      
    print(" ".join(nwords)) 

