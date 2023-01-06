from termcolor import colored

class_list = [
    {
        'name': 'Knight',
        'health_points': 15,
        'skill_points': 10,
        'attack': 3,
        'player_name': '',
        'skills': [{
            'name': 'Shield Bash',
            'attack': 2,
            'special': True,
            'dis': (
                'deals 2 damage and has 50% chance to inflict stun '
                'causing opponent to miss next turn. Costs 2SP'),
            'cost': 2},
            {
            'name': 'Mighty Blow',
            'attack': 5,
            'special': False,
            'dis': (
                'You Swing your sword with both hands dealing '
                'severe damage. Costs 4SP'),
            'cost': 4
        }]
    },
    {
        'name': 'mage',
        'health_points': 10,
        'skill_points': 20,
        'attack': 2,
        'player_name': '',
        'skills': [{
            'name': 'Fireball',
            'attack': 5,
            'special': False,
            'dis': (
                'Deals 4 damage to opponent. Costs: 3SP'),
            'cost': 4},
            {
            'name': 'Heal',
            'attack': 0,
            'special': False,
            'dis': 'Heal yourself by 5HP. Costs: 5SP',
            'cost': 5
        }]
    },
    {
        'name': 'archer',
        'health_points': 10,
        'skill_points': 15,
        'attack': 3,
        'player_name': '',
        'skills': [{
            'name': 'Double shot',
            'attack': 5,
            'special': None,
            'dis': 'Deals 5 damage. Costs 3SP',
            'cost': 3},
            {
            'name': 'cripple',
            'attack': 3,
            'special': True,
            'dis': ('Deal damage and 50% chance to stun '
                    'opponent. Costs: 4SP'),
            'cost': 4
            }]
    }
]

party_list = []


monster_list = [
    {
        'name': 'Goblin',
        'health_points': 10,
        'attack': 2,
        'skills': [{'name': 'Slice', 'attack': 3}]
    },
    {
        'name': 'Brigand',
        'health_points': 15,
        'attack': 2,
        'skills': [{'name': 'Cleave', 'attack': 3}]
    },
    {
        'name': 'Demon Guard',
        'health_points': 20,
        'attack': 3,
        'skills': [{'name': 'Rend', 'attack': 4}]
    },
    {
        'name': 'Dark Dragon',
        'health_points': 30,
        'attack': 4,
        'skills': [{'name': 'Dragon Breath', 'attack': 6}]
    }
]

item_list = {
    'health_potion': 3,
    'skill_potion': 3,
    'coin': 50
}
