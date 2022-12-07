#Project

import random
l=["Rock","Paper","Scissor"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game start....
1 Yes
2 No | Exit
Enter: '''))
    if uc==1:
        for a in range(1,6):
            print("Round:",a)
            userInput=int(input('''
1 Rock
2 Paper
3 Scissor
Enter: '''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Paper"
            elif userInput==3:
                uchoice="Scissor"
            else:
                uchoice="Invalid"

            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("Computer Win")
                ccount=ccount+1
        if ucount==ccount:
            print("Final Game Draw....")
            print("User Score",ucount)
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("You Win the game....")
            print("User Score",ucount)
            print("Computer Score",ccount)
        else:
            print("Computer Win the game....")
            print("User Score",ucount)
            print("Computer Score",ccount)
            
                  
    elif uc==2:
        print("You have Exit the Game")
        break
    else:
        print("Enter 1 or 2")
    
