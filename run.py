from termcolor import colored
import os 

current_question = 0
current_monster = 0

class_list = [
    {
        'name': 'Knight',
        'health_points': 15,
        'skill_points': 10,
        'attack': 3,
        'skills': [{'name': 'shield bash', 'attack': 2, 'special': 0, 'dis': 'deals 2 damage and has 50% chance to inflict stun causing opponent to miss next turn. Costs 2sp', 'cost': 2}, 
        {'name': 'heros shield', 'attack': 0, 'special': 1, 'dis': 'Take no damage if attacked next enemy turn. Costs 3SP', 'cost': 3}],
        'dex': 3
    },
    {
        'name': 'mage',
        'health_points': 10,
        'skill_points': 20,
        'attack': 2,
        'skills': [{'name': 'Fireball', 'attack': 5, 'special': None, 'dis': 'Deals 4 damage to opponent. Costs: 3SP', 'cost': 4},
        {'name': 'Heal', 'attack': 0, 'special': 2, 'dis': 'Heal any chosen ally by 5HP. Costs: 3SP', 'cost': 3}],
        'dex': 3
    },
    {
        'name': 'archer',
        'health_points': 10,
        'skill_points': 15,
        'attack': 2,
        'skills': [{'name': 'Double shot', 'attack': 4, 'special': None, 'dis': 'Deals 4 damage. Costs 3SP', 'cost': 3},
        {'name': 'cripple', 'attack': 2, 'special': 3, 'dis': 'Deal damage and also weaken enemy attack by 1. Costs: 4SP', 'cost': 4}],
        'dex': 5
    }
]

party_list = [

]

monster_list = [

]

item_list = {
    'health_potion': 3,
    'skill_potion': 3,
    'coin': 50
}


question_list = [
    {
        'question': f"Start your adventure! Do you go {colored('left', 'red')}, {colored('right', 'red')}, {colored('forward', 'red')}",
        'answers': ['left', 'right', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        'question': 'You see a goblin do you fight, run, talk',
        'answers': ['fight', 'run', 'talk'],
        'ans1': ['You turn left', 1, 'fight'],
        'ans2': ['You turn tail and run away from the goblin back to the crossroads', 0, 'no_fight'],
        'ans3': ['You try talk to the goblin', 2, 'no_fight']
    },
    {
        'question': 'The Goblin demands you give him a health potion if you wish to pass. Do you fight, give, run',
        'answers': ['fight', 'give', 'run'],
        'ans1': ['You turn left', 1, 'fight'],
        'ans2': ['You hand over 1 potion', 3, 'no_fight'],
        'ans3': ['You turn tail and run away from the goblin back to the crossroads', 0, 'no_fight'],
        'lose_item': 'health_potion'
    },
    {
        'question': 'With the goblin behind you, you come across a small campsite littered with a few caravans to your left. You also notice a riverbed to your right. do you try talk to the camp, check the river, or press forward',
        'answers': ['talk', 'river', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        'question': '5',
        'answers': ['a', 'b', 'c'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
]

def intro():
    intro_text = colored('\n WELCOME TO ZORK AND DRAGONS! \n', 'green')
    print(intro_text)
    print(f"A text based rpg adventure where you choose 3 party members and set off on a quest to defeat the dark dragon. At every stop in your journey you will be given 3 options to progress. the terminal command needed for each one will be highlighted in {colored('red', 'red')} like this!\n")

    print('You will choose a team of 3 from 4 different adventurers and start of with 3 health potions, 3 skill potions and 50 coins\n')

    print(f"At any time during your quest type {colored('item', 'green')} to open your inventory and see your current health and skill points\n")



    question = input(f"please enter {colored('y', 'red')} to progress to the your character selection\n")

    if question == 'y':
        os.system('clear')
        return

    else:
        print('Invalid option. Try again!\n')

def char_select(number):
    os.system('clear')
    knight = class_list[0]
    mage = class_list[1]
    archer = class_list[2]
    print(f"Choose your {number} character!")

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
                
        else: 
            print('Invalid option. Try again!\n')



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




