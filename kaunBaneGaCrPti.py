questions = [ 
    ["who is the prime minister of bihar?", "NK" , "MK" , "PK" ,"LK" ,"NONE", 1],

["who was the first person to go to moon?" , "nel armstrong" , "kalpana chawala" , "arundati roa" , "munasi das" , 1],

["what is the name of the powerhouse of the cell?" , "flamina", "mitrocondia", "losita" , "musnasi", 2],

["who is the prime minister of bihar?", "NK" , "MK" , "PK" ,"LK" ,"NONE", 1],

["who was the first person to go to moon?" , "nel armstrong" , "kalpana chawala" , "arundati roa" , "munasi das" , 1],

["what is the name of the powerhouse of the cell?" , "flamina", "mitrocondia", "losita" , "musnasi", 2],

["what is the name of the world tallest statue?", "satue of librty" ,"statue of unity" , "statue of grace", "statue of freedom" , 2],

["who is the prime minister of bihar?", "NK" , "MK" , "PK" ,"LK" ,"NONE", 1],

["who was the first person to go to moon?" , "nel armstrong" , "kalpana chawala" , "arundati roa" , "munasi das" , 1],

["what is the name of the powerhouse of the cell?" , "flamina", "mitrocondia", "losita" , "musnasi", 2],

["what is the name of the world tallest statue?", "satue of librty" ,"statue of unity" , "statue of grace", "statue of freedom" , 2],

["who is the prime minister of bihar?", "NK" , "MK" , "PK" ,"LK" ,"NONE", 1],

["who was the first person to go to moon?" , "nel armstrong" , "kalpana chawala" , "arundati roa" , "munasi das" , 1],

["what is the name of the powerhouse of the cell?" , "flamina", "mitrocondia", "losita" , "musnasi", 2],

["how many planets are there in solar system?", "nine","eight","seven","five" , 2],
]

levels = [1000, 2000, 3000, 5000, 10000,    20000, 40000, 80000, 160000, 320000,   640000, 1250000, 2500000, 5000000, 10000000]

money = 0

for i in range (0, len(questions)):

    question = questions[i]
    print(f"\n\nquestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question [1]}     b. {question [2]}") 
    print(f"c. {question [3]}     d.{question[4]}")

    reply = int (input("enter your answer(1-4) or to quit:\n"))
    if (reply ==0 ):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"correct answer, you have won rs. {levels[i]}")
        
        if (i==4):
            money = 10000
            # print("congratulation for winner all the best for future")
        elif(i==9):
            money = 320000
            # print("congratulation for winning all the best for future")
        elif(i==14):
            money = 10000000
            # print("congratulation for winning all the best for future you are the winner of this season !!!!!!!!!!!!!!!!!! :)")
    else:
        print("wrong answer!")
        break



print (f"you take home money is {money}")
print("thanku for your contribution")

    
    















# questions = [
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
# ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
  
#   question = questions[i]
#   print(f"\n\nQuestion for Rs. {levels[i]}")
#   print(f"a. {question[1]}          b. {question[2]} ")
#   print(f"c. {question[3]}          d. {question[4]} ")
#   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
#   if (reply == 0):
#     money = levels[i-1]
#     break
#   if(reply == question[-1]):
#     print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(i == 4):
#       money = 10000
#     elif(i == 9):
#       money = 320000
#     elif(i == 14):
#       money = 10000000
#   else:
#     print("Wrong answer!")
#     break 

# print(f"Your take home money is {money}")