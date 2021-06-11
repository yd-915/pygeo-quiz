print("Welcome to a pop geography quiz!")

challenger = input("Are you ready? ")
if challenger.lower() != "yes":
    print('Oh well maybe next time')
    quit()
    
else:
    print("here we go!")
    score = 0
    
answer = input("Where is Canada? ")
if answer.lower() != 'north america':
    print('False')
else:
    print('True')
    score +=1
    
answer = input("Where is Sudan? ")
if answer.lower() != 'north africa':
    print('False')
else:
    print('True')
    score +=1
    
answer = input("Where is Germany? ")
if answer.lower() != ' west europe':
    print('False')
else:
    print('True')
    score +=1
    
answer = input("Where is Tajikistan? ")
if answer.lower() != 'central asia':
    print('False')
else:
    print('True')
    score +=1
    
answer = input("Where is Saudi Arabia? ")
if answer.lower() != 'west asia':
    print('False')
else:
    print('True')
    score +=1

answer = input("Where is Congo Republic? ")
if answer.lower() != 'central africa':
    print('False')
else:
    print('True')
    score +=1

answer = input("Where is Bosnia and Herzegovina? ")
if answer.lower() != ' east europe':
    print('False')
else:
    print('True')
    score +=1

    

    
print("You got " + str(score) + " correct")
print("You got " + str((score / 4) * 100) + "% ")