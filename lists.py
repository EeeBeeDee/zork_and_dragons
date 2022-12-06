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
        'attack': 3,
        'skills': [{'name': 'Double shot', 'attack': 5, 'special': None, 'dis': 'Deals 4 damage. Costs 3SP', 'cost': 3},
        {'name': 'cripple', 'attack': 2, 'special': 3, 'dis': 'Deal damage and also weaken enemy attack by 1. Costs: 4SP', 'cost': 4}],
        'dex': 5
    }
]

party_list = []

monster_list = []

item_list = {
    'health_potion': 3,
    'skill_potion': 3,
    'coin': 50
}


