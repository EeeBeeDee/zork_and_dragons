




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
        question = input(f"{question_list[list]['question']} \n")

        if question in question_list[list]['answers']:
            if question == question_list[list]['answers'][0]:
                print('you turn left')
                ask_question(1)
                
        else: 
            print('Invalid option. Try again!')







ask_question(0)
