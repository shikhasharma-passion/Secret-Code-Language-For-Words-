import random

word = (input("enter your word :"))

if len(word)>3:
    chars ="abcdefghijklmnoqrstuvwxyz"
    makeitlist = list(word)
    listHaiYeh = makeitlist 
    firstLetterKoNiklnaHa =  listHaiYeh.pop(0)
    listHaiYeh.append(firstLetterKoNiklnaHa)
    print(listHaiYeh)
    word = ''.join(listHaiYeh)
    print(word)

    start_chars = ''.join(random.choices(listHaiYeh, k=3))
    end_chars = ''.join(random.choices(listHaiYeh, k=3))
    final = start_chars +word+ end_chars 
    print("our secret coded word is here")
    print(''.join(final))
else:
    makeitlist = list(word)
    listHaiYeh = makeitlist
    listHaiYeh.reverse()
    print("our secret coded word is here")
    print(''.join(listHaiYeh))