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
        'question': 'Start your adventure! Do you go left, right, forwards',
        'answers': ['left', 'right', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        'question': 'You see a goblin do you fight, run, talk',
        'answers': ['fight', 'run', 'talk'],
        'ans1': ['You turn left', 1, 'fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        'question': '3',
        'answers': ['a', 'b', 'c'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        'question': '4',
        'answers': ['a', 'b', 'c'],
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


def ask_question(list):
    while True:
        question_obj = question_list[list]
        question = input(f"{question_obj['question']}. \n \n ")
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




ask_question(0)
