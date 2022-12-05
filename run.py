from termcolor import colored
import os 

from lists import class_list, party_list, monster_list, question_list, item_list

current_question = 0
current_monster = 0



def intro():
    intro_text = colored('\nWELCOME TO ZORK AND DRAGONS! \n', 'green')
    print(intro_text)
    print(f"A text based rpg adventure where you choose 3 party members and set off on a quest to defeat the dark dragon. At every stop in your journey you will be given 3 options to progress. the terminal command needed for each one will be highlighted in {colored('red', 'red')} like this!\n")

    print('You will choose a team of 3 from 4 different adventurers and start of with 3 health potions, 3 skill potions and 50 coins\n')

    print(f"At any time during your quest type {colored('item', 'green')} to open your inventory and see your current health and skill points\nOr type {colored('quit', 'red')} to restart the game and come back to this screen!\n\n")



    while True:
        question = input(f"please enter {colored('y', 'red')} to progress to the your character selection\n")

        if question == 'y':
            os.system('clear')
            return
        else:
            os.system('clear')
            print('Invalid option. Try again!\n')

def char_select(number):
    os.system('clear')
    knight = class_list[0]
    mage = class_list[1]
    archer = class_list[2]
    print(f"Choose your {number} character!\n\n")

    while True:
        print(f"{knight['name']}\nHP: {knight['health_points']}\nSkill Points: {knight['skill_points']}\nSkills:\n{colored(knight['skills'][0]['name'], 'green')} - {knight['skills'][0]['dis']}\n{colored(knight['skills'][1]['name'], 'green')} - {knight['skills'][1]['dis']}\n\n")

        print(f"{mage['name']}\nHP: {mage['health_points']}\nSkill Points: {mage['skill_points']}\nSkills:\n{colored(mage['skills'][0]['name'], 'green')} - {mage['skills'][0]['dis']}\n{colored(mage['skills'][1]['name'], 'green')} - {mage['skills'][1]['dis']}\n\n")

        print(f"{archer['name']}\nHP: {archer['health_points']}\nSkill Points: {archer['skill_points']}\nSkills:\n{colored(archer['skills'][0]['name'], 'green')} - {archer['skills'][0]['dis']}\n{colored(archer['skills'][1]['name'], 'green')} - {archer['skills'][1]['dis']}\n\n")

        choice = input(f"Do you choose {colored('knight', 'red')}, {colored('mage', 'red')}, {colored('archer', 'red')}\n")

        if choice == 'knight':
            return knight
        elif choice == 'mage':
            return mage
        elif choice == 'archer':
            return archer
        else:
            os.system('clear')
            print('Invalid option. Try again!\n')



def ask_question(list):
    while True:
        question_obj = question_list[list]
        question = input(f"{question_obj['question']}. \n \n ")
        os.system('clear')
        global current_question
        global current_monster

        if question in question_obj['answers']:
            if question == question_obj['answers'][0]:
                if question_obj['ans1'][2] == 'fight':
                    print('you are in a fight \n \n')
                else:
                    print(f"{question_obj['ans1'][0]} \n")
                    current_question = question_obj['ans1'][1]
                    ask_question(current_question)

            elif question == question_obj['answers'][1]:
                print(f"{question_obj['ans2'][0]} \n")
                current_question = question_obj['ans2'][1]
                ask_question(current_question)

            elif question == question_obj['answers'][2]:
                print(f"{question_obj['ans3'][0]} \n")
                current_question = question_obj['ans3'][1]
                ask_question(current_question)
        elif question == 'item':
            item_screen()  
        elif question == 'quit':
            current_question = 0
            current_monster = 0
            party_list = []
            main()  
        else: 
            print('Invalid option. Try again!\n')

def item_screen():
    p1 = party_list[0]
    p2 = party_list[1]
    p3 = party_list[2]

    print(f"You have:\n\n{item_list['health_potion']} Health Potions\n{item_list['skill_potion']} Skill potions\n{item_list['coin']} Coins\n\n")

    print(f"{p1['name']}\nHP: {p1['health_points']}\nSkill Points: {p1['skill_points']}\nSkills:\n{colored(p1['skills'][0]['name'], 'green')} - {p1['skills'][0]['dis']}\n{colored(p1['skills'][1]['name'], 'green')} - {p1['skills'][1]['dis']}\n\n")

    print(f"{p2['name']}\nHP: {p2['health_points']}\nSkill Points: {p2['skill_points']}\nSkills:\n{colored(p2['skills'][0]['name'], 'green')} - {p2['skills'][0]['dis']}\n{colored(p2['skills'][1]['name'], 'green')} - {p2['skills'][1]['dis']}\n\n")

    print(f"{p3['name']}\nHP: {p3['health_points']}\nSkill Points: {p3['skill_points']}\nSkills:\n{colored(p3['skills'][0]['name'], 'green')} - {p3['skills'][0]['dis']}\n{colored(p3['skills'][1]['name'], 'green')} - {p3['skills'][1]['dis']}\n\n")


    input('\nHit any key to return')
    os.system('clear')
    ask_question(current_question) 

def stun():
    print()

def main():
    intro()
    player1 = char_select('first')
    player2 = char_select('second')
    player3 = char_select('third')
    party_list.append(player1)
    party_list.append(player2)
    party_list.append(player3)
    os.system('clear')
    # print(party_list)
    ask_question(0)

main()




