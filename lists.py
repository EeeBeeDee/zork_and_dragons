from termcolor import colored


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
        {'name': 'Heal', 'attack': 0, 'special': 2, 'dis': 'Heal any chosen ally by 5HP. Costs: 5SP', 'cost': 5}],
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