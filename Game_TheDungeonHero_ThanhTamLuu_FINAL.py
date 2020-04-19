#!/usr/bin/env python
# coding: utf-8

# In[53]:


"""

DocString: 

    A) Introduction: 
    Let me introduce you to the greatest game of all time - The Dungeon Hero!
    Your friend has been kidnapped by a monster that has been haunting your town 
    and you followed the monster to its dungeon. Follow your friend's voice to 
    save his/her life but be careful... the monster is right behind you. 
    
    In this game, you will have to go through three dungeons in which you will 
    have to make life-and-death decisions.
    
    Dungeon 1: Choosing the left or right path.
    Dungeon 2: Door choice and answering questions.
    Dungeon 3: Picking up the right box with a special key. 
    
    While creating this game, I was inspired by my favorite k-drama 
    'Memories of the Alhambra' and the most recent movie that I watched
    'It Chapter Two'. 
    
    B) Known Bugs and/or Error:
    None.
    
"""

import time
from sys import exit
import random
from random import randint

def game_start():
    global savior_name
    global rescuee_name
    global fear_creature
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the greatest game of all time - The Dungeon Hero!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input('<Press Enter to Continue>\n')
    print("Yes, that is YOU who I am talking about!\n")
    time.sleep(.5)       # Using time.sleep() function to enhance the story flow.
    print("\tSo...")
    time.sleep(.3)
    print("\n\t\t What's")
    time.sleep(.3)
    print("\n\t\t\t going")
    time.sleep(.3)
    print("\n\t\t\t\t on?")
    time.sleep(1)
    print("""
Your city has been endangered by a monster for the past few weeks. 
After you saw the monster kidnapping your friend, you followed it to its dungeon. 
You lost its trace but you are hearing your friend's voice...\n
""")
    input('<Press Enter to Continue>\n')
    
    print("\nHello? Who is there?\n")
    savior_name = input('Input your name: \n').capitalize()
    time.sleep(.3)
    print(f"\n{savior_name}?? Ah.. My head... What.. What is my name?\n")
    rescuee_name = input("Input your friend's name: \n").capitalize()
    time.sleep(.3)
    print(f"""
\nYes, my name is {rescuee_name}. I remember now...
""")
    print(f"""
Oh no, {savior_name}, you shouldn't have followed me here!\n
""") 
    print("Have you seen the monster? What... What was it?\n")
    fear_creature = input("Input the creature you fear the most: \n").capitalize()
    time.sleep(.3)      
    print(f"\nOh, you're right. It was a big scary {fear_creature}!\n")
    time.sleep(.5)
    print(f"\t{savior_name}, please, save me!!\n")
          
    input('\n<Press Enter to Continue>\n')
             
    print(f"{rescuee_name}: Oh no, I can hear its steps!\n")
    time.sleep(1) 
    print(f"{fear_creature}: Ha ha ha, I'm coming for you!\n")
    time.sleep(1)
    
    #######################################
    # While loop: Space shuttle countdown #
    #######################################
    
    count = 3
    
    while count > 0:
        print(count)
        count -= 1
        
        input("[ Steps approaching ... ]\n\n<Press Enter to Continue>\n")
        
    print(f"{rescuee_name}: Hurry!!! You have to run - NOW!\n")
    
    input('<Press Enter to Continue>\n') 
    dungeon_1()  
          
def dungeon_1(): 
    print("""
You are now in Dungeon 1 and only have two paths to run to. 
Which path would you like to take?\n
    1) left
    2) right
        
""")
    
    #############################################################
    # Conditional statement based on what path a player chooses #
    #############################################################
    
    choice = input(">  \n").lower()
    
    if "1" in choice or "1)" in choice or "left" in choice:
        print(f"\nYou escaped the {fear_creature} for now!\n")
        input('<Press Enter to Continue>\n')
        dungeon_2()
        
    elif "2" in choice or "2)" in choice or "right" in choice:
        print(f"""
        \nOh no! You have encountered the {fear_creature} and were not able to escape.\n
        """)
        fail()
        
    else:
        print("\nSomething went wrong. Please try again.\n")
        input('<Press Enter to Try Again>\n')
        dungeon_1()
          
def dungeon_2():
    print(f"""
You managed to escape the {fear_creature} in Dungeon 1 but the {fear_creature}
is still going after you. You have reached the end of the path and you are now
in Dungeon 2. You see three doors in front of you and you have to go through 
one of these in order to carry on.\n
Which door would you like to open?\n
    1) not scary 
    2) very scary
        
""")
    
    #############################################################
    # Nested conditional statements based on the player's input #
    #############################################################
    
    choice = input(">  \n").lower()
    
    if "1" in choice or "1)" in choice or "not" in choice or "not scary" in choice:
        print("""
\nNot scary door it is! Well.. It is not easy to pass this door so easily 
after all. You have to correctly answer a question first.\n
""")
        print("""
        What is the shape of this underground dungeon?\n
            1) circle
            2) triangle
            
        """)
        
        answer = input(">  \n").lower()
        
        if "1" in answer or "1)" in answer or "circle" in answer:
            print(f"\n{fear_creature}: Ha ha ha, that is not correct. I guess")
            print("you will have to stay here with me to explore more.\n")
            print("The door has closed and you cannot escape.")
            fail()
        
        elif "2" in answer or "2)" in answer or "triangle" in answer:
            print(f"\nGreat job, {savior_name}. That is correct!\n")
            print("You are so close to your friend now!\n")
            input('<Press Enter to Continue>\n')
            dungeon_3()
        
        else:
            print("\nSomething went wrong. Please try again.\n")
            input('<Press Enter to Try Again>\n')
            dungeon_2()
        
        
    elif "2" in choice or "2)" in choice or "very" in choice or "very scary" in choice:
        print("""
\nWow, what a brave move! But... 
You still have to answer a question to continue.\n
""")
        print(f"""
        What does the {fear_creature} like to eat most - after human beings?\n 
            1) banana
            2) paper
            
        """)
              
        answer = input(">  \n").lower()
        
        if "1" in answer or "1)" in answer or "banana" in answer:
            print(f"\n{fear_creature}: Ha ha ha, that is not correct. I guess")
            print("you will have to stay here with me to get to know me better.\n")
            print("The door has closed and you cannot escape.")
            fail()
        
        elif "2" in answer or "2)" in answer or "paper" in answer:
            print(f"\nGreat job, {savior_name}. That is correct!\n")
            print("You are so close to your friend now!\n")
            input('<Press Enter to Continue>\n')
            dungeon_3()
        
        else:
            print("\nSomething went wrong. Please try again.\n")
            input('<Press Enter to Try Again>\n')
            dungeon_2()
        
    else:
        print("\nSomething went wrong. Please try again.\n")
        input('<Press Enter to Try Again>\n')
        dungeon_2()
            
def dungeon_3():
    print("You have just entered the last dungeon!\n")
    input('<Press Enter to Continue>\n')
    print(f"""
But before you can save {rescuee_name} who is still being locked up,
you have to choose the right box with the special key that will
close all the paths that led up to this point, unlock {rescuee_name},
and finally open the gate for you and {rescuee_name} to escape.
\n""")
    print("Important: The special key changes its box location every time") 
    print("someone makes an unsuccessful attempt to get the key.\n") # This is a hint that guessing the correct number is random and that the key is not always in the same box.
    input('<Press Enter to Continue>\n')
    print(f"You only have TWO guesses before the {fear_creature} catches up")
    print(f"with you and thwarts your only way to save {rescuee_name}!\n")
    print("." * 10)
    print("\nThere's no time to waste. Hurry up!!\n")
    input('<Press Enter to Continue>\n')
    
    box_number = random.randint(1,3)    # This is for random number guessing.
    guesses = 2     # This is giving the player 2 chances to guess.
    
    while guesses > 0:
        
        #####################
        # Nested while loop #
        #####################
        
        while guesses >0:
            print(f"""
Which box do you think the special key is in?\n
        1, 2, or 3?
            
""")
        
            box_input = input("Input a number from 1 to 3:  \n")
            
            try:
                box_input = int(box_input)
                
                if type(box_input) == int:
                    break
            
            except ValueError:      # This is for whenever the player inputs a value that is not an integer.
                print("\nThat is an invalid entry. Please try again.")
    
        if box_input == box_number:
            print(f"""
{rescuee_name}: {savior_name}!! I can't belive you saved me!\n
\tYOU ARE A REAL DUNGEON HERO!
""")
            print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
""")
            print("""
Congratulations \n\t\tand \n\t\t\tthanks \n\t\t\t\tfor \n\t\t\t\t\tplaying!
""")
            print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
""")
                
            input('\n<Press Enter to Exit>\n')
            exit(0)
            break
            
        elif box_input != box_number:
            
            #################################
            # Nested conditional statements #
            #################################
            
            if guesses == 1:
                print("""
Oh no, you're out of guesses.
            
""")
                guesses -= 1
                fail_1()
                      
            elif guesses > 0:
                guesses -= 1
                print(f"""
Oh no, that's incorrect. You have {guesses} guess(es) remaining.

""")
                      
            else: 
                print("\nSomething went wrong. Please try again.\n")
                dungeon_3()
                
        else:
            print("\nSomething went wrong. Please try again.\n")
            dungeon_3()    
              
def fail():
    
    print("It looks like you have failed your mission.")
    
    print("Would you like to play again? (Yes/No)")
    answer = input("> ")
    answer = answer.lower()
    
    if answer == 'yes':
        dungeon_1()   # Trying to enhance user experience 
                      # by taking the player to the first decision tree
                      # so that the player does not have to read the intro again.
        
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~")
        print("Thank you for trying!")
        print("~~~~~~~~~~~~~~~~~~~~~\n")
        exit(0)
        
def fail_1():
    
    print("Would you like to guess again? (Yes/No)")
    answer = input("> ")
    answer = answer.lower()
    
    if answer == 'yes':
        
        dungeon_3()   # Trying to making winning more enjoyable
                      # by letting the player guess again instead of 
                      # having to play the entire game from the beginning.
        
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~")
        print("Thank you for trying!")
        print("~~~~~~~~~~~~~~~~~~~~~\n")
        exit(0)
        
        
game_start()

