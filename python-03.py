import random
secret = random.randint(1,10)
print ("---------danran----------")
temp = input("please input you choise chanse: ")
chanse = int(temp)
while chanse > 0 :
    number = input("please input number: ")
    guess = int(number)
    if guess == secret:
        print ("you are right")
        break
    elif guess > secret:
        print ("you are error")
        print ("you input number is high")
    else:
        print ("you are error")
        print ("The input number is low")
    chanse=chanse-1
print ("game over")
    
