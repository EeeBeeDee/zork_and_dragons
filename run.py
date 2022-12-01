current_question = 0

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


question_list = [
    {
        'question': 'Start your adventure! Do you go left, right, forwards',
        'answers': ['left', 'right', 'forwards']
    },
    {
        'question': 'you see a goblin do you fight, run, talk',
        'answers': ['a', 'b', 'c']
    },
    {
        'question': '3',
        'answers': ['a', 'b', 'c']
    },
    {
        'question': '4',
        'answers': ['a', 'b', 'c']
    },
    {
        'question': '5',
        'answers': ['a', 'b', 'c']
    },
]


def ask_question(list):
    while True:
        question_obj = question_list[list]
        question = input(f"{question_obj['question']}.")

        if question in question_obj['answers']:
            if question == question_obj['answers'][0]:
                print('you turn left \n')
                global current_question
                current_question = 1
                ask_question(current_question)
                
        else: 
            print('Invalid option. Try again!\n')


def stun():
    print()




ask_question(0)
