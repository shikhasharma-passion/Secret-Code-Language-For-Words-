st = input("Enter Message :")   
words = st.split(" ")
# write 'True' for encoding and 'False' for decoding
coding = True
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
