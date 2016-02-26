######################################################################
#TODO: Author: Crystal Rudd
#TODO: username: ruddc
#
# Assignment: L1
# Purpose:
######################################################################
# Acknowledgements:
#   This program utilizes inspiration from Dr. Jan Pearce
######################################################################

def balls(balls_left):
    '''This function is used to keep track of how many balls there are
    balls_left is exactly what it says, the amount of balls that are left to play with'''
    
    print("There are " + str(balls_left) + " ball(s) left.") #tells the user how many balls are left
    return balls_left #returns balls_left 

def user():
    '''This function is used to keep track of user input'''
    sel_str = raw_input("How many balls do you choose? 1-4: ")
    sel_int = int(sel_str) #converts the user's input into an int to be used later
    
    #The if statement checks to see if the user input is in the parameters
    if (sel_int == 1) or (sel_int == 2) or (sel_int == 3) or (sel_int == 4):
        print("You chose " + sel_str + " ball(s).")
        return sel_int #returns the users choice
    else: #The esle statement has a loop that loops until the user chooses a valid number
        while (sel_int != 1) and (sel_int != 2) and (sel_int!=3) and (sel_int != 4):
            sel_str = raw_input("That is not a valid selection. Please choose either 1, 2, 3, or 4!\n")
            sel_int = int(sel_str)
        print("You chose " + sel_str + " balls(s).")
        return sel_int #returns the user's choice
        
def mth(chosen_ball, t_ball):
    '''This is the function for the math of the user, taking how many balls they chose and subtracting it from how many balls there are left and returning a new num.
    chosen_ball is the number of balls that were chosen by either the computer or the player
    t_ball is the total amount of balls left to chose from'''
    balls_left = int(t_ball) - int(chosen_ball) #subtracting the total amount of balls from the chosen amount will give you a new total called balls_left
    return int(balls_left) #returning an integer

def comp_turn(t_ball):
    '''the computer needs to land on a number that makes the total ball divisible by 5 with no remainder.
    t_ball is the total number of balls that are left'''
    num_balls = t_ball%5
    comp_choice = 0
    while (num_balls != 0):
        t_ball = t_ball - 1
        comp_choice += 1
        num_balls = t_ball%5
        #print("There are " + str(num_balls) + " remaining")
        #print("comp_choice = " + str(comp_choice) + "!")
    print("The computer chose " +str(comp_choice) + " ball(s)")
    return comp_choice

def main():
    '''This function calls all of the other functions to create the game of Nimm. '''
    
    balls_left = balls(15)
    while(balls_left > 0):
        user_choice = user()
        balls_left = mth(user_choice, balls_left)
        balls(balls_left)
        comp_choice = comp_turn(balls_left)
        balls_left = mth(comp_choice, balls_left)
        balls(balls_left)
    print("The Computer will always win! Sorry about your luck.")
    
main()
