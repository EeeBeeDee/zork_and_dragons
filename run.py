from termcolor import colored
import os
import copy

from lists import class_list, party_list, item_list
from questions import question_list
from battle import battle_start

current_question = 0
in_battle = False


def intro():
    """
    Acts as intro and tutorial to mechanics.
    Function deals with only the first terminal screen.
    """

    intro_text = colored('\nWELCOME TO ZORK AND DRAGONS! \n', 'green')
    print(intro_text)
    print(
        ("A text based rpg adventure where you choose 3 party members\nand "
            "set off on a quest to defeat the dark dragon.\n"
            "At every stop in "
            "your journey you will be given 3 options to progress.\nThe "
            "terminal command needed for each one will be highlighted in "
            f"{colored('red', 'red')} like this!\n")
    )

    print(
        ('You will choose a team of 3 from 4 different adventurers and '
            'start of with\n3 health potions, 3 skill potions '
            'and 50 coins\n')
    )

    print(
        (f"At any time during your quest type {colored('item', 'green')} to "
            "open your inventory\n"
            "and see your current health and skill points "
            f"\nOr type {colored('quit', 'red')} to restart the "
            "game and come back to this screen!\n\n")
    )

    while True:
        question = input(
                    (f"please enter {colored('y', 'red')} to progress "
                        "to the character selection\n")
                    )

        if question == 'y':
            os.system('clear')
            return
        else:
            os.system('clear')
            print('Invalid option. Try again!\n')


def char_select(number):
    """
    Function to create player party using templates from class_list.
    Prints info on each class and uses while loop to insure valid
    selections are made.
    Function is run individually 3 times in main() to place 3 chosen characters
    in party_list using deepcopy from copy.
    """

    os.system('clear')
    knight = class_list[0]
    mage = class_list[1]
    archer = class_list[2]
    print(f"Choose your {number} character!\n\n")

    while True:
        print(
            (f"{knight['name']}\nHP: {knight['health_points']}\n"
                f"Skill Points: {knight['skill_points']}\n"
                f"Skills:\n{colored(knight['skills'][0]['name'], 'green')} "
                f"- {knight['skills'][0]['dis']}\n"
                f"{colored(knight['skills'][1]['name'], 'green')} "
                f"- {knight['skills'][1]['dis']}\n\n")
        )

        print(
            (f"{mage['name']}\nHP: {mage['health_points']}\n"
                f"Skill Points: {mage['skill_points']}\n"
                f"Skills:\n{colored(mage['skills'][0]['name'], 'green')} "
                f"- {mage['skills'][0]['dis']}\n"
                f"{colored(mage['skills'][1]['name'], 'green')} "
                f"- {mage['skills'][1]['dis']}\n\n")
        )

        print(
            (f"{archer['name']}\nHP: {archer['health_points']}\n"
                f"Skill Points: {archer['skill_points']}\n"
                f"Skills:\n{colored(archer['skills'][0]['name'], 'green')} "
                f"- {archer['skills'][0]['dis']}\n"
                f"{colored(archer['skills'][1]['name'], 'green')} "
                f"- {archer['skills'][1]['dis']}\n\n")
        )

        choice = input(
            (f"Do you choose {colored('knight', 'red')}"
                f", {colored('mage', 'red')},"
                f" {colored('archer', 'red')}\n")
        )

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
    """
    Takes all relevant data from each question object in question_list.
    Forms questions and options in terminal.
    As game is question based it also deals with progression, Gameover etc.
    Checks if typed input is part of available answers for each question
    using while loop.
    If special answers like "fight" are chosen it runs corresponding function
    before returning to loop
    Entire game is based off of this functions loop.

    """
    while True:
        question_obj = question_list[list]
        question = input(f"{question_obj['question']}. \n \n ")
        os.system('clear')
        global current_question
        global party_list
        global item_list

        if question in question_obj['answers']:
            if question == question_obj['answers'][0]:
                if question_obj['ans1'][2] == 'fight':
                    current_monster = question_obj['monster_number']
                    battle_start(current_monster)
                    current_question = question_obj['ans1'][1]
                    ask_question(current_question)
                elif question_obj['ans1'][2] == 'pay':
                    item_list['coin'] = item_list['coin'] - 30
                    current_question = question_obj['ans1'][1]
                    ask_question(current_question)
                elif question_obj['ans1'][2] == 'rest':
                    party_list[0]['health_points'] = party_list[0]['health_points'] + 10  # noqa
                    party_list[1]['health_points'] = party_list[1]['health_points'] + 10  # noqa
                    party_list[2]['health_points'] = party_list[2]['health_points'] + 10  # noqa
                    item_list['coin'] = item_list['coin'] - 20
                    current_question = question_obj['ans1'][1]
                    ask_question(current_question)
                else:
                    print(f"{question_obj['ans1'][0]} \n")
                    current_question = question_obj['ans1'][1]
                    ask_question(current_question)

            elif question == question_obj['answers'][1]:
                if question_obj['ans2'][2] == 'give':
                    item_list['health_potion'] = item_list['health_potion'] - 1
                    print(f"{question_obj['ans2'][0]} \n")
                    current_question = question_obj['ans2'][1]
                    ask_question(current_question)
                else:
                    print(f"{question_obj['ans2'][0]} \n")
                    current_question = question_obj['ans2'][1]
                    ask_question(current_question)

            elif question == question_obj['answers'][2]:
                if question_obj['ans3'][2] == 'gold':
                    item_list['coin'] = item_list['coin'] + 10
                    print(f"{question_obj['ans3'][0]} \n")
                    current_question = question_obj['ans3'][1]
                    ask_question(current_question)
                if question_obj['ans3'][2] == 'game_over':
                    print(f"{question_obj['ans3'][0]} \n")
                    print('Game Over! PLease try again!\n')
                    input('Press enter to restart!\n')
                    os.system('clear')
                    current_question = 0
                    current_monster = 0
                    party_list = []
                    item_list = {
                        'health_potion': 3,
                        'skill_potion': 3,
                        'coin': 50
                    }
                    main()

                else:
                    print(f"{question_obj['ans3'][0]} \n")
                    current_question = question_obj['ans3'][1]
                    ask_question(current_question)

        elif question == 'item':
            item_screen()
        elif question == 'quit':
            current_question = 0
            current_monster = 0
            party_list = []
            item_list = {
                'health_potion': 3,
                'skill_potion': 3,
                'coin': 50
            }
            main()
        else:
            print('Invalid option. Try again!\n')


def item_screen():
    """
    Shows party status including health, inventory and skills
    returns to ask_question() loop upon hitting enter.
    """

    p1 = party_list[0]
    p2 = party_list[1]
    p3 = party_list[2]

    print(
        (f"You have:\n\n{item_list['health_potion']} "
            f"Health Potions\n{item_list['skill_potion']} "
            f"Skill potions\n{item_list['coin']} Coins\n\n")
    )

    print(
        (f"{p1['name']} -- {p1['player_name']}\n"
            f"HP: {p1['health_points']}\nSkill Points: {p1['skill_points']}\n"
            f"Skills:\n{colored(p1['skills'][0]['name'], 'green')} "
            f"- {p1['skills'][0]['dis']}\n"
            f"{colored(p1['skills'][1]['name'], 'green')} "
            f"- {p1['skills'][1]['dis']}\n\n")
    )

    print(
        (f"{p2['name']} -- {p2['player_name']}\n"
            f"HP: {p2['health_points']}\nSkill Points: {p2['skill_points']}\n"
            f"Skills:\n{colored(p2['skills'][0]['name'], 'green')} "
            f"- {p2['skills'][0]['dis']}\n"
            f"{colored(p2['skills'][1]['name'], 'green')} "
            f"- {p2['skills'][1]['dis']}\n\n")
    )

    print(
        (f"{p3['name']} -- {p3['player_name']}\n"
            f"HP: {p3['health_points']}\nSkill Points: {p3['skill_points']}\n"
            f"Skills:\n{colored(p3['skills'][0]['name'], 'green')} "
            f"- {p3['skills'][0]['dis']}\n"
            f"{colored(p3['skills'][1]['name'], 'green')} "
            f"- {p3['skills'][1]['dis']}\n\n")
    )

    input('\nHit enter to return')
    os.system('clear')
    ask_question(current_question)


def name_select():
    """
    Assigns chosen names to each party character.
    Asked individually 3 times in main()
    """

    party_list[0]['player_name'] = input('Name your first character\n\n')
    party_list[1]['player_name'] = input('\nName your second character\n\n')
    party_list[2]['player_name'] = input('\nName your third character\n\n')


def main():
    intro()
    player1 = copy.deepcopy(char_select('first'))
    player2 = copy.deepcopy(char_select('second'))
    player3 = copy.deepcopy(char_select('third'))
    os.system('clear')
    party_list.append(player1)
    party_list.append(player2)
    party_list.append(player3)
    name_select()
    print(player1)
    print(player2)
    print(player3)
    print(party_list)
    os.system('clear')
    ask_question(0)


main()
