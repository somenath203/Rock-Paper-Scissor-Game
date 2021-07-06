import random

while(True):

    print("<-------------------ROCK-PAPER-SCISSOR Game------------------->")
    print("\n")
    nooft = int(input("Enter the number of rounds you want to play :- "))
    syscount = 0
    usercount = 0

    while(nooft):
        while(True):
            print('''
            Enter your choice :-
            1) Press (r) or (R) for Rock.
            2) Press (s) or (S) for Scissor.
            3) Press (p) or (P) for Paper.
            ''')
            urchoice = input()
            if(urchoice=='s' or urchoice=='S' or urchoice=='r' or urchoice=='R' or urchoice=='p' or urchoice=='P'):
                break
            elif(urchoice!='s' or urchoice!='S' or urchoice!='r' or urchoice!='R' or urchoice!='p' or urchoice!='P'):
                print("Your choice is invalid. Please select a correct option.")
                continue

        sys = ["r","p","s"]
        syschoice = random.choice(sys)

        # Printing User's Choice
        if(urchoice == "r" or urchoice == "R"):
            print("Your Choice :- Rock")
        elif(urchoice == "p" or urchoice == "P"):
            print("Your Choice :- Paper")
        elif(urchoice == "s" or urchoice == "S"):
            print("Your Choice :- Scissor")
        # Printing System's Choice
        if(syschoice == "r" or syschoice == "R"):
            print("System's Choice :- Rock")
        elif(syschoice == "p" or syschoice == "P"):
            print("System's Choice :- Paper")
        elif(syschoice == "s" or syschoice == "S"):
            print("System's Choice :- Scissor")
        
        # FOR ROCK
        if((urchoice == 'r' and syschoice == 'p') or (urchoice == 'R' and syschoice == 'p')):
            print("System WON because system chose paper and you chose rock.")
            syscount = syscount + 1
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        elif((urchoice == 'r' and syschoice == 's') or (urchoice == 'R' and syschoice == 's')):
            print("You WON because you chose paper and system chose rock.")
            usercount = usercount + 1
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        elif((urchoice == 'r' and syschoice == 'r') or (urchoice == 'R' and syschoice == 'r')):
            print("DRAW because both system and you chose same i.e. rock.")
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        # FOR SCISSOR
        elif((urchoice == 's' and syschoice == 'p') or (urchoice == 'S' and syschoice == 'p')):
            print("You WON because you chose scissor and system chose paper.")
            usercount = usercount + 1
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        elif((urchoice == 's' and syschoice == 'r') or (urchoice == 'S' and syschoice == 'r')):
            print("System WON because you chose scissor and system chose paper.")
            syscount = syscount + 1
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        elif((urchoice == 's' and syschoice == 's') or (urchoice == 'S' and syschoice == 's')):
            print("DRAW because both system and you chose same i.e. scissor.")
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        # FOR PAPER
        elif((urchoice == 'p' and syschoice == 'r') or (urchoice == 'P' and syschoice == 'r')):
            print("You WON because you chose paper and system chose rock.")
            usercount = usercount + 1
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        elif((urchoice == 'p' and syschoice == 's') or (urchoice == 'P' and syschoice == 's')):
            print("System WON because you chose paper and system chose scissor.")
            syscount = syscount + 1
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")
        elif((urchoice == 'p' and syschoice == 'p') or (urchoice == 'P' and syschoice == 'p')):
            print("DRAW because both system and you chose same i.e. paper.")
            nooft = nooft - 1
            print("You have",nooft,"attempts left.")

    print("\n")
    print("<------------------------------RESULT------------------------------>")
    print("\n")
    print("Your Score :- ",usercount)
    print("System's Score :- ",syscount)
    print("\n")
    if(syscount>usercount):
        print("System WON...")
    if(usercount>syscount):
        print("Crongrats!!! You WON.")
    if(syscount==usercount):
        print("The match is a tie.")
    

    print("Do you wan to play once more? Press 'y' or 'Y' for YES or press any other key for NO.")
    choice = input()
    if(choice=='y' or choice=='Y'):
        continue
    else:
        print("Thanks for playing Rock-Paper-Scissor. We hope to see you again. Take care.")
        break
