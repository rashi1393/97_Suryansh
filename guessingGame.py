import random
print("Number Guessing Game")

#randint fuction to generate thr randon number 1 to 9 
number = random.randint(1, 9)

#number of chances to be given to user to gess to number 
#or it is the intups gives user into intup  box  here number of 
chances =0

print("Guess a number(between 1 to 9):")

#While loop counts the numbers of chances 
while chances < 5:

    # enter a number between 1 to 9
    guess = int(input("Enter your guess:- "))

    #compare the user enter number with number to be guessed 

    if guess == number:
    #if number entered by the is same as the generated
    #number by randint function then breakfrom the loop 
    #control statement "break" 
        print("Congratulation you Won!!")
        break

    #check if the user entered number is smaller the generated number
    elif guess < number:
        print("Your guess was to low: Guess higher numbr than", guess)

    #the user enter number is greater than the generated number 
    else:
        print("Youe guess was too high: Guess a number lower than", guess)  

    #Increse the value of chanc by 1 
    chances += 1

    #Check whether the user guessed the correct number 
    if not chances < 5:
        print("YOU LOSE!!! The number is", number)

