from termcolor import colored
import os 

current_question = 0
current_monster = 0

class_list = [
    {
        'name': 'Knight',
        'health_points': 15,
        'skill_points': 10,
        'skills': [{'name': 'shield bash', 'attack': 2, 'special': 1}],
        'attack': 3,
        'dex': 3
    },
    {
        'name': 'Knight',
        'health_points': 15,
        'skill_points': 10,
        'skills': [{'name': 'shield bash', 'attack': 2, 'special': 1}],
        'attack': 3,
        'dex': 3
    },
    {
        'name': 'Knight',
        'health_points': 15,
        'skill_points': 10,
        'skills': [{'name': 'shield bash', 'attack': 2, 'special': 1}],
        'attack': 3,
        'dex': 3
    }
]

monster_list = [

]


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
    ask_question(0)

main()




