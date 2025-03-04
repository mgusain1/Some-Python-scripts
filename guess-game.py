# A very small game to play with yourself 


import random
print("Hi my name is AL, what is yours ?")
name = input()
print(f"Hi {name} how are you")
print(f"Hi {name }lets play a game shall we?\nPick a number between 0 and 10\nYou will get 7 tries")

secret = random.randint(0,10)
for i in range(0,7):
    print("please pick a number?")
    try:
        number = int(input())
        if number > secret:
            print("You chose High")
        elif number < secret:
            print("You chose too low")
        else:
            break
    except Exception as e:
        print(e, "look at your error now")
        
if secret == number:
    print("You chose right")
else:
    print(f"The number i was thinking of was {guess}")
        
