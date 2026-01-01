# import time

# timestramp = int(time.strptime('%H:%M:%S'))
# print(timestramp)
# if timestramp <12:
#     print("GOOD MORNING MAM") 
# elif  12 <= timestramp >=16:
#     print("Good Afternoon")
# elif  16 <= timestramp >=20:
#     print("GOOD EVENING ")
# else :
#     print("GOOD NIGHT")
# print("bye bye")

import time

timestramp = int(time.strftime('%H'))
print("current time:" , time.strftime('%H:%M:%S'))

timestramp = int(time.strftime('%H'))
print("current time:",time.strftime('%H:%M:%S'))

timestramp = int (time.strftime('%M'))
print(timestramp)

timestramp = int (time.strftime('%S'))
print(timestramp)

if 0<=timestramp <12:
    print("GOOD MORNING")
elif 12<= timestramp <16:
    print("goood afternoon")
elif 16<= timestramp <20:
    print("good evening ")

else:
    print("good night  ")

print("Thanks for your Attention")
