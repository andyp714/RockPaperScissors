'''
Created on Oct 28, 2020
Rock Paper Scissors
Narration: Lets the user play a game of Rock, Paper, Scissors. In singleplayer, the user selects an option then the computer chooses one as well. The winner is then decided and the score is changed. In multiplayer, 2 players select an option and see who wins. At the end of the game, the players are able to decife if they want to play again.
Log 1.0: Initial Version
Log 1.1: Score Feature Added, Easter Egg
Log 1.2: Multiplayer Feature added, supports 2 players and a play again option
Log 1.3: Fixed select mode bug, code used to accept non valid modes
Log 1.4: Added a rigged option to make sure player 1 wins most of the time. To access, input 'Multiplayer Mode'
Bugs: None
Features: Play Again, Score Counter, Hello Easter Egg, Multiplayer mode, Secret rigged mode for player 1
@author: apauley24
'''

import random                                                                                                       #Imports random to set up random variables#



def main():  
    
                                                                                                           
    #routine to check choices                                                                                                       #Sets up a main code that goes on start, welcomes user and selects mode#
    print("Welcome to Rock-Paper-Scissors")
    mode = input("What Mode would you like to play, Multiplayer(M) Or Singleplayer(S)?")
    if mode == "singleplayer" or mode == "Singleplayer" or mode == "S" or mode == "s":                              
        rock_paper_scissors()                                                                                       
    elif mode == "Multiplayer" or mode == "multiplayer" or mode == "M" or mode == "m":                              
        multiplayer()                                                                                              
    elif mode == "Multiplayer Mode":                                                                                
        multiplayer_rigged()                                                                                       
    else:
        print("You have to put in a valid mode.")                                                                   
        
        
def multiplayer_rigged():                                                                                           
    loop_M = True                           #bool for play again option                                                                                                
    while loop_M == True:  
        #Routine for inputting variables and checking if valid#                 
        rpsm_check = True                   #bool for checking for valid variables                                                                         
        while rpsm_check == True:           
            player1_rps = input("Player One, Please input Rock, Paper, or Scissors")                                
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")                                                                                              #Creates space between the player 1 and 2 inputs so that Player 2 cannot see Player 1's input#
            player2_rps = input("Player Two, Please input Rock, Paper, or Scissors")                                #Asks PLayer 2 for their input#
            player1_rps = player1_rps.capitalize()
            player2_rps = player2_rps.capitalize()                                                                  #sets the variable 
            
            if player1_rps == "Rock":
                if player2_rps == "Rock":
                    rpsm_check = False
                elif player2_rps == "Paper":
                    rpsm_check = False
                elif player2_rps == "Scissors":
                    rpsm_check = False
                else:
                    rpsm_check = True
                    print("Please only input the supported inputs")
            elif player1_rps == "Paper":
                if player2_rps == "Rock":
                    rpsm_check = False
                elif player2_rps == "Paper":
                    rpsm_check = False
                elif player2_rps == "Scissors":
                    rpsm_check = False
                else:
                    rpsm_check = True
                    print("Please only input the supported inputs")
            elif player1_rps == "Scissors":
                player1_rps = "Scissors"
                if player2_rps == "Rock":
                    rpsm_check = False
                elif player2_rps == "Paper":
                    rpsm_check = False
                elif player2_rps == "Scissors":
                    rpsm_check = False
                else:
                    rpsm_check = True
                    print("Please only input the supported inputs")
            else:
                rpsm_check = True
                print("Please only input the supported inputs")
        #Routine to decide who wins using random numbers, giving player 1 an advantage#
        random_int = random.randint(1, 4)
        if random_int < 4:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        #Routine for play again option
        play_again_M = input("Want to play again? Input 'Y' or 'Yes'")
        if play_again_M == "Y" or play_again_M == "y" or play_again_M == "Yes" or play_again_M == "yes":
            loop_M = True           #Bool for loop
        else:
            loop_M = False          #bool for loop


def multiplayer():    
    loop_M = True                   #bool for loop for play again
    while loop_M == True: 
        #Routine for checking valid variables and input           
        rpsm_check = True           #Bool for variable check#
        while rpsm_check == True:
            player1_rps = input("Player One, Please input Rock, Paper, or Scissors")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            player2_rps = input("Player Two, Please input Rock, Paper, or Scissors")
            player1_rps = player1_rps.capitalize()
            player2_rps = player2_rps.capitalize()
            
            if player1_rps == "Rock":
                if player2_rps == "Rock":
                    rpsm_check = False
                elif player2_rps == "Paper":
                    rpsm_check = False
                elif player2_rps == "Scissors":
                    rpsm_check = False
                else:
                    rpsm_check = True
                    print("Please only input the supported inputs")
            elif player1_rps == "Paper":
                if player2_rps == "Rock":
                    rpsm_check = False
                elif player2_rps == "Paper":
                    rpsm_check = False
                elif player2_rps == "Scissors":
                    rpsm_check = False
                else:
                    rpsm_check = True
                    print("Please only input the supported inputs")
            elif player1_rps == "Scissors":
                player1_rps = "Scissors"
                if player2_rps == "Rock":
                    rpsm_check = False
                elif player2_rps == "Paper":
                    rpsm_check = False
                elif player2_rps == "Scissors":
                    rpsm_check = False
                else:
                    rpsm_check = True
                    print("Please only input the supported inputs")
            else:
                rpsm_check = True
                print("Please only input the supported inputs")
        #Routine for deciding who wins#
        if player1_rps == player2_rps:
            print("You Tied")
        elif player1_rps == "Rock" and player2_rps == "Paper":
            print("Player 2 wins!")
        elif player1_rps == "Rock" and player2_rps == "Scissors":
            print("Player 1 wins!")
        elif player2_rps == "Rock" and player1_rps == "Paper":
            print("Player 1 wins!")
        elif player2_rps == "Rock" and player1_rps == "Scissors":
            print("Player 2 wins!")
        elif player1_rps == "Paper" and player2_rps == "Scissors":
            print("Player 2 wins!")
        elif player1_rps == "Paper" and player2_rps == "Rock":
            print("Player 1 wins!") 
        elif player2_rps == "Paper" and player1_rps == "Rock":
            print("Player 2 wins!")
        elif player2_rps == "Paper" and player1_rps ==  "Scissors":
            print("Player 1 wins!")
        elif player1_rps == "Scissors" and player2_rps == "Rock":
            print("Player 2 wins!")
        elif player1_rps == "Scissors" and player2_rps == "Paper":
            print("Player 1 wins!")
        elif player2_rps == "Scissors" and player1_rps == "Rock":
            print("Player 1 wins!")
        elif player2_rps == "Scissors" and player1_rps == "Paper":
            print("Player 2 wins!")
        #Routine for playing again option, uses bool from top of code#
        play_again_M = input("Want to play again? Input 'Y' or 'Yes'")
        if play_again_M == "Y" or play_again_M == "y" or play_again_M == "Yes" or play_again_M == "yes":
            loop_M = True
        else:
            loop_M = False
            
         

def rock_paper_scissors():
        
        
        loop = True     #Bool for looping, play again
        score = 0       #Sets score to 0, so a score feature could be used
        while loop ==  True:
            #Routine for checking if inputs are valid#
            rps_check = True        #Bool for checking inputs#
            while rps_check == True:
                rps = input("Please Input Rock, Paper or Scissors")
                if rps == 'Rock' or rps == 'rock':
                    rps = "Rock"
                    rps_check = False
                elif rps == 'Paper' or rps == 'paper':
                    rps = "Paper"
                    rps_check = False
                elif rps == 'Scissors' or rps == 'scissors':
                    rps = "Scissors"
                    rps_check = False
            #Routine for Computer decides their choice then decides who wins#
            rps_list = ["Rock", "Paper", "Scissors"]
            rand_choice = random.choice(rps_list)
            print("You chose", rps )
            print("Your opponent chose", rand_choice)
            if rps == rand_choice:
                print("You Tied.", "Your Score Is:", score)
            elif rps == "Rock" and rand_choice == "Scissors":
                score = score +1
                print("You Won.", "Your Score is:", score)
            elif rps == "Rock" and rand_choice == "Paper":
                score = score -1
                print("You Lost.", "Your Score is:", score)
            elif rps == "Paper" and rand_choice == "Scissors":
                score = score -1
                print("You Lost.", "Your Score is:", score)
            elif rps == "Paper" and rand_choice == "Rock":
                score = score +1
                print("You Won.", "Your Score is:", score)
            elif rps == "Scissors" and rand_choice == "Rock":
                score = score -1
                print("You Lost.", "Your Score is:", score)
            elif rps == "Scissors" and rand_choice == "Paper":
                score = score +1
                print("You Win.", "Your Score is:", score)
            #Routine for play again option with Easter Egg#
            playagain = input("Input 'Yes' to play again.")
            if playagain == "yes" or playagain == "Yes":
                loop = True
            elif playagain == "Hello":
                print("(^_^)/")
            else:
                print("Thanks For Playing")
                loop = False
                
        
      
    
    
    
    
    
    

if __name__ == "__main__":
    main()