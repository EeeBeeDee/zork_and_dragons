from termcolor import colored
from lists import class_list, party_list, monster_list,  item_list

"""
Each question holds all data needed to progress in game.

'question' = Question printed in terminal to player.
'answers' = Three possible inputs that will progress the game.
'ansX' = Holds info needed to progress after corresponding
answer from 'answers' is entered.
    ansx[0] = Message displayed to player upon input
    ansx[1] = The next numbered question object in question_list to
    be passed into the main ask_question() function
    ansx[2] = Used to run functions after certain answers.
    To enter battles etc.

'lose_item' = Signifies which item could be lost from
inventory after this question
'monster_number' = Signifies which monster object in monster
list is passed into battle function after said question.
"""
question_list = [

    {
        # 0 - beginning
        'question': (
            f"Start your adventure! Do you go {colored('left', 'red')}, "
            f"{colored('forwards', 'red')}, {colored('right', 'red')}"
        ),
        'answers': ['left', 'forwards', 'right'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You head forwards', 13, 'no_fight'],
        'ans3': [(
                'You turn Right, the road crumbles beneath your feet '
                'the whole party fall in and die'
                'a horrible death!'), 0, 'game_over']
    },
    {
        # 1 - goblin
        'question': (
            f"You see a goblin do you {colored('fight', 'red')}, "
            f"{colored('run', 'red')}, {colored('talk', 'red')}"
        ),
        'answers': ['fight', 'run', 'talk'],
        'ans1': ['', 3, 'fight'],
        'ans2': [(
            'You turn tail and run away from the goblin back to '
            'the crossroads', 0, 'no_fight'
            )],
        'ans3': ['You try talk to the goblin', 2, 'no_fight'],
        'monster_number': 0
    },
    {
        # 2 - goblin - talk
        'question': (
            "The Goblin demands you give him a health potion if you "
            f"wish to pass. Do you {colored('fight', 'red')}, "
            f"{colored('give', 'red')}, {colored('run', 'red')}"
            ),
        'answers': ['fight', 'give', 'run'],
        'ans1': ['', 3, 'fight'],
        'ans2': ['You hand over 1 potion', 3, 'give'],
        'ans3': [(
            'You turn tail and run away from the goblin  '
            f'to the crossroads', 0, 'no_fight'
            )],
        'lose_item': 'health_potion',
        'monster_number': 0
    },
    {
        # 3 - after goblin - see camp
        'question': (
            "With the goblin behind you, you come across a small "
            "campsite littered with a few caravans to your left. "
            "You also notice a riverbed to your right. "
            f"do you try {colored('talk', 'red')} to the camp, "
            f"check the {colored('river', 'red')}, "
            f"or press {colored('forward', 'red')}"
        ),
        'answers': ['talk', 'river', 'forwards'],
        'ans1': [(
            'You call out to see if anyone is in the '
            'camp', 4, 'no_fight'
            )],
        'ans2': ['You head towards the river', 5, 'no_fight'],
        'ans3': ['You head forwards along the path', 6, 'no_fight']
    },
    {
        # 4 - checking camp
        'question': (
            "Two men approach, they seem friendly enough but you "
            "notice a bit of blood on one mans clothes, you exchange "
            "pleasantries and tell them why you have set "
            "out on your quest. They seem overjoyed that you plan "
            "to take down the dragon and offer to let you rest. "
            f"Do you {colored('rest', 'red')} here, decide to "
            f"check the {colored('river', 'red')} behind you "
            f"or press {colored('forward', 'red')}"
        ),
        'answers': ['rest', 'river', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': [(
            'You double back and cross the path to head towards '
            'the river', 5, 'no_fight')
            ],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 5 - riverbed
        'question': (
            "Approaching the riverbed you notice a small rickety boat "
            "you could potentially use to get down stream. "
            "You could also just use it to cross the river and "
            f"continue on foot. Do you take the {colored('boat', 'red')} "
            f"down stream, use it to {colored('cross', 'red')} the river, "
            f"or turn back and press {colored('forwards', 'red')} along "
            "the path you just left"
            ),
        'answers': ['boat', 'cross', 'forwards'],
        'ans1': [(
            'You all hop into the boat one at a time trying to capsize '
            'it before you even depart. After a few minutes and some '
            'wet feet you depart down the river'), 6, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 6 - sailing down the river
        'question': (
            "After quite some time and smoothing sailing dulling "
            "the parties alertness, the party notices the sound of "
            "a waterfall, but just too late. The boat rushes over "
            f"the edge {colored('--BOOM--','white', 'on_red')}, everyone "
            "awakes washed onto a shore. you hear the hustle and "
            "bustle of a town just ahead and notice a bridge to the "
            f"right, Do you head towards the {colored('town', 'red')}, "
            f"decide to take the {colored('bridge', 'red')}, or head back "
            f"the way you came following the {colored('river', 'red')}"
        ),
        'answers': ['town', 'bridge', 'river'],
        'ans1': [(
            'You step into the main plaza of the town of '
            'Riverstone'), 7, 'no_fight'],
        'ans2': [(
            'Crossing the bridge you end up back where it all began, you '
            'decide to rest awhile before starting again'), 0, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 7 - entering town
        'question': (
            "You arrive at the town or Riverstone"
            "As you walk in you notice an inn and a general shop. "
            "You ponder whither you have time to rest or shop or should "
            "you press on towards the mountain. "
            f"Do you enter the {colored('inn', 'red')}, "
            f"decide to {colored('shop', 'red')} or head towards the castle "
            f"by the {colored('mountain', 'red')}"
        ),
        'answers': ['inn', 'shop', 'mountain'],
        'ans1': ['You enter the inn', 8, 'no_fight'],
        'ans2': ['you enter the shop', 0, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 8 - inn
        'question': (
            "As you walk in you hear a table talking about a man escaping "
            "from the dragon castle not long ago. You are greeted by "
            "the innkeeper and offered a room for 20 gold. Do you "
            f"{colored('rest', 'red')}, join the {colored('table', 'red')} "
            f"to hear more or return to the {colored('town', 'red')} center."
            ),
        'answers': ['rest', 'table', 'town'],
        'ans1': [(
            'You all sleep well. Felling fully refreshed you step out into '
            'the town at dawn ready to continue'), 7, 'no_fight'],
        'ans2': [(
            'You sit down at the table to inquire about what you '
            'overheard'), 9, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 9 - table
        'question': (
            "The men all fall silent as you sit down. After reassuring "
            "them you mean no harm, you ask about this escape. An older "
            "man begins to tell you of a secret tunnel. One he is will "
            "to show you. For a price... 30 gold coins Do you "
            f"{colored('pay', 'red')}, {colored('threaten', 'red')}  "
            "him to show you or return to the entrance of "
            f"the {colored('inn', 'red')}."
            ),
        'answers': ['pay', 'threaten', 'inn'],
        'ans1': [(
            'Handing over the coin you demand we leave at once '
            'to which he agrees'), 10, 'pay'],
        'ans2': [(
            'You sit down at the table to inquire about what you '
            'overheard', 9, 'no_fight')],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 10 - secret entrance
        'question': (
            "After a few hours Journey you reach a tiny cave in the side "
            "of a hill, the old man commends your bravery and gives you "
            "one last piece of advise 'Beware the gold plated door...'\n"
            "Barely squeezing through the tiny gap you all press on"
            "Eventually coming across a trap door, upon climbing through"
            "you enter the keep proper in what looks to be a torture"
            "chamber of some sort with its door ajar. "
            "peaking out you hear armour clad footsteps to the left, "
            "what seems to be an unkept, unlit hallway straight ahead "
            "and a freezing cold breeze coming from the path to the right."
            f"Do you go {colored('left', 'red')}, "
            f"{colored('straight', 'red')}  "
            f"or {colored('right', 'red')}."
            ),
        'answers': ['left', 'straight', 'right'],
        'ans1': [(
            'You run into an armed deamon guard! No choice but to '
            'fight '), 11, 'fight'],
        'ans2': [(
            'You sit down at the table to inquire about what you '
            'overheard', 9, 'no_fight')],
        'ans3': ['You head forwards', 3, 'no_fight'],
        'monster_number': 2
    },
    {
        # 11 - outside throne room - guard
        'question': (
            "You realize he was protecting the dark dragons throne room "
            "It sinks in that this is now the end of your journey..."
            f"Do you step into the {colored('throne', 'red')} room, "
            f"continue exploring the {colored('castle', 'red')}  "
            "or now quaking in your boots decide to "
            f"{colored('give', 'red')} up and quit?"
            ),
        'answers': ['throne', 'castle', 'give'],
        'ans1': [(
            'Everyone takes a deep breath and steps into the gold laden '
            'throne room '), 12, 'no_fight'],
        'ans2': [(
            'You sit down at the table to inquire about what you '
            'overheard'), 9, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 12 - throne room
        'question': (
            "Surrounded by piles of riches on all sides a massive shadow"
            "looms from the ceiling, a terrifying rumbling voice speaks, "
            "powerful enough to make your armour rattle and your ears bleed..."
            "'Finally someone has come, you look quite confident. "
            "Do you really think you can best me in combat?, or perhaps "
            "you make know the sacred words? It does not matter,"
            "your time in this world is at an end!'"
            f"Do you {colored('fight', 'red')}, "
            f"{colored('speak', 'red')} the holy words "
            f"or {colored('beg', 'red')} for your life?"
            ),
        'answers': ['fight', 'speak', 'beg'],
        'ans1': [(
            'Everyone takes a deep breath and steps into the gold laden '
            'throne room '), 14, 'fight'
            ],
        'ans2': [(
            'You sit down at the table to inquire about what you '
            'overheard', 9, 'no_fight')],
        'ans3': [(
            'You bow your heads and cry for your lives'
            'Not noticing the dragon readying its flame'
            'breath... You all cook in your armour'), 3, 'game_over'],
        'monster_number': 3
    },
    {
        # 13 - Brigand on the bridge
        'question': (
            "On the bridge headed into A nearby town you come across "
            "a brigand threatening some merchants, "
            f"do you {colored('fight', 'red')} him off, "
            f"{colored('ignore', 'red')} and carry on forwards, "
            f"or {colored('threaten', 'red')} him yourself?"
        ),
        'answers': ['fight', 'ignore', 'threaten'],
        'ans1': ['', 7, 'fight'],
        'ans2': [(
            'You ignore it all and continue on your way ',
            7, 'no_fight'
            )],
        'ans3': [(
                'You Threaten the Thief, he pleads for his life'), 7, 'gold'],
        'monster_number': 1
    },
]
