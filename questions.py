from termcolor import colored

question_list = [
    {
        # 0
        'question': f"Start your adventure! Do you go {colored('left', 'red')}, {colored('right', 'red')}, {colored('forward', 'red')}",
        'answers': ['left', 'right', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 1
        'question': f"You see a goblin do you {colored('fight', 'red')}, {colored('run', 'red')}, {colored('talk', 'red')}",
        'answers': ['fight', 'run', 'talk'],
        'ans1': ['You turn left', 1, 'fight'],
        'ans2': ['You turn tail and run away from the goblin back to the crossroads', 0, 'no_fight'],
        'ans3': ['You try talk to the goblin', 2, 'no_fight']
    },
    {
        # 2
        'question': f"The Goblin demands you give him a health potion if you wish to pass. Do you {colored('fight', 'red')}, {colored('give', 'red')}, {colored('run', 'red')} fight, give, run",
        'answers': ['fight', 'give', 'run'],
        'ans1': ['You turn left', 1, 'fight'],
        'ans2': ['You hand over 1 potion', 3, 'no_fight'],
        'ans3': ['You turn tail and run away from the goblin back to the crossroads', 0, 'no_fight'],
        'lose_item': 'health_potion'
    },
    {
        # 3
        'question': f"With the goblin behind you, you come across a small campsite littered with a few caravans to your left. You also notice a riverbed to your right. do you try {colored('talk', 'red')} to the camp, check the {colored('river', 'red')}', or press {colored('forward', 'red')}",
        'answers': ['talk', 'river', 'forwards'],
        'ans1': ['You call out to see if anyone is in the camp', 4, 'no_fight'],
        'ans2': ['You head towards the river', 5, 'no_fight'],
        'ans3': ['You head forwards along the path', 6, 'no_fight']
    },
    {
        # 4
        'question': f"Two men approach, they seem friendly enough but ou notice a bit of blood on one mans clothes, you exchange pleasantries and tell them why you have set out on your quest. They seem overjoyed that you plan to take down the dragon and offer to let you rest. Do you {colored('rest', 'red')} here, decide to check the {colored('river', 'red')} behind you or press {colored('forward', 'red')}",
        'answers': ['rest', 'river', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 5, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 5
        'question': f"Approaching the riverbed you notice a small rickety boat you could potentially use to get down stream. You could also just use it to cross the river and continue on foot. Do you take the {colored('boat', 'red')} down stream, use it to {colored('cross', 'red')}' the river, or turn back and press {colored('forwards', 'red')} along the path you just left",
        'answers': ['boat', 'cross', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
]