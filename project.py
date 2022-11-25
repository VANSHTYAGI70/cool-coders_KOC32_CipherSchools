import random

x=int(input("Enter the lower range: "))
print('********************************')
y=int(input("Enter the upper range: "))
print('********************************')
score=0
n=0

while(n<3):
    userinput= int(input("Enter your Number: "))
    
    if userinput not in range(x,y+1):
        print("Please enter a number which is in the given range.")
    
    
    while (x<=userinput<=y):
        n+=1
        number= random.randrange(x,y+1)
        if (userinput>number):
            print("Have one more try. Your Guess was too high.")
            print("Generated Number: ",number)
            print('********************************')
            break
        elif(userinput<number):
            print("Have one more try. Your Guess was too low.")
            print("Generated Number: ",number)
            print('********************************')
            break
        
        elif (userinput==number):
            print("Generated number",number)
            print("Your Guess Number is equal to generated number.")
            print('********************************')
        
            score+=1
            break
            


if(score>0):
    print("Congrat's")
else:
    print("Better luck Next Time!")
print("Your score is: ",score)