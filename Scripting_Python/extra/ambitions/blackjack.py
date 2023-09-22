#!/usr/bin/python
import random
sum = 0

#generate card
cardnum=random.randint(1,13)
if cardnum == 13:
    print("your first card is an ace.\n")
    answerA = input("which value do you choose?\n1/11\n")
    '''if isinstance(answerA, str) == True:
        print("you've entered a string. I do not tolerate this nonsense and therefor will terminate this script.")
        exit()
    else: '''
    if int(answerA) == 1:
            cardnum = 1
            sum += cardnum
            print("your sum is now: {}\n".format(sum))
    elif int(answerA) == 11:
            cardnum = 11
            sum += cardnum
            print("your sum is now: {}\n".format(sum))
    else:
            print("you've entered a wrong value. I do not tolerate this and therefor will terminate this script.")
            exit()
else: 
    print("your first card is {}".format(cardnum))
    sum += cardnum



while sum < 21:
    answer = input("would you like to draw another card?\n Yes/No\n")
    Answer = answer.upper()

    if Answer == "YES" :
        cardnum=random.randint(1,13)
        if cardnum == 13:
            print("your card is an ace.\n")
            if sum > 10:
                cardnum = 1
                print("\nYou have to pick the value of one.")
            
            else:
                answerA = input("which value do you choose?\n 1/11\n")
                if int(answerA) == 1: 
                    cardnum = 1
                    print("your sum is now: {}\n".format(sum))
                elif int(answerA) == 11: 
                    cardnum = 11
                    print("your sum is now: {}\n".format(sum))
                else:
                    print("You entered a wrong value.\n")
            sum += cardnum
        else: sum += cardnum
        print("your new card is {}, and your sum is now {}".format(cardnum, sum))
    elif Answer == "NO" : break

    else : 
        print("Write yes or no in long, please.\n")
        continue

if sum == 21 : print("BLACKJACK")
elif sum > 21 : print("you got burned.")
else:
    if 17 <= sum < 21 : 
        print("congrats, you beat the dealer.")
        if sum <= 20 : 
            print("\nand even got a nice score!")
            if sum == 20 : 
                print("\nand nearly got the perfect 21 mark!")
    else : print("dealer wins")