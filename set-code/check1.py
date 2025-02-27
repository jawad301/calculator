import random 
nump = random.randint (10,99)
n =  int (input ("Enter a 2 digit Number :"))
while n !=10 :
    num = nump 
    cor = 0
    while num%10 :
        numc = num%10
        nc = n%10
        num = num // 10
        n = n//10
        if numc ==nc :
            cor = cor + 1
    if cor == 2:
        print ("Congrate you guessed the Number ")
        break
    else :
        print ("%d Number was guessed right ."%cor)
        n =  int (input ("Enter a 2 digit Number :"))
else :
    print ("You quit the game.")
        
        