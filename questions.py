from termcolor import colored
from lists import class_list, party_list, monster_list,  item_list

question_list = [
    {
        # 0 - beginning
        'question': f"Start your adventure! Do you go {colored('left', 'red')}, {colored('right', 'red')}, {colored('forward', 'red')}",
        'answers': ['left', 'right', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 1 - goblin
        'question': f"You see a goblin do you {colored('fight', 'red')}, {colored('run', 'red')}, {colored('talk', 'red')}",
        'answers': ['fight', 'run', 'talk'],
        'ans1': ['You turn left', 1, 'fight'],
        'ans2': ['You turn tail and run away from the goblin back to the crossroads', 0, 'no_fight'],
        'ans3': ['You try talk to the goblin', 2, 'no_fight']
    },
    {
        # 2 - goblin - talk
        'question': f"The Goblin demands you give him a health potion if you wish to pass. Do you {colored('fight', 'red')}, {colored('give', 'red')}, {colored('run', 'red')} fight, give, run",
        'answers': ['fight', 'give', 'run'],
        'ans1': ['You turn left', 1, 'fight'],
        'ans2': ['You hand over 1 potion', 3, 'no_fight'],
        'ans3': ['You turn tail and run away from the goblin back to the crossroads', 0, 'no_fight'],
        'lose_item': 'health_potion'
    },
    {
        # 3 - after goblin - see camp
        'question': f"With the goblin behind you, you come across a small campsite littered with a few caravans to your left. You also notice a riverbed to your right. do you try {colored('talk', 'red')} to the camp, check the {colored('river', 'red')}, or press {colored('forward', 'red')}",
        'answers': ['talk', 'river', 'forwards'],
        'ans1': ['You call out to see if anyone is in the camp', 4, 'no_fight'],
        'ans2': ['You head towards the river', 5, 'no_fight'],
        'ans3': ['You head forwards along the path', 6, 'no_fight']
    },
    {
        # 4 - checking camp
        'question': f"Two men approach, they seem friendly enough but ou notice a bit of blood on one mans clothes, you exchange pleasantries and tell them why you have set out on your quest. They seem overjoyed that you plan to take down the dragon and offer to let you rest. Do you {colored('rest', 'red')} here, decide to check the {colored('river', 'red')} behind you or press {colored('forward', 'red')}",
        'answers': ['rest', 'river', 'forwards'],
        'ans1': ['You turn left', 1, 'no_fight'],
        'ans2': ['You double back and cross the path to head towards the river', 5, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
    {
        # 5 - riverbed
        'question': f"Approaching the riverbed you notice a small rickety boat you could potentially use to get down stream. You could also just use it to cross the river and continue on foot. Do you take the {colored('boat', 'red')} down stream, use it to {colored('cross', 'red')}' the river, or turn back and press {colored('forwards', 'red')} along the path you just left",
        'answers': ['boat', 'cross', 'forwards'],
        'ans1': ['You all hop into the boat one at a time trying to capsize it before you even depart. After a few minutes and some wet feet you depart down the river', 6, 'no_fight'],
        'ans2': ['You turn Right', 2, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
     {
        # 6 - sailing down the river
        'question': f"After quite some time and smoothing sailing dulling the parties alertness, the party notices the sound of a waterfall, but just too late. The boat rushes over the edge {colored('--BOOM--','white', 'on_red')}, everyone awakes washed onto a shore. you hear the hustle and bustle of a town just ahead and notice a bridge to the right, Do you head towards the {colored('town', 'red')}, decide to take the {colored('bridge', 'red')}, or head back the way you came following the {colored('river', 'red')}",
        'answers': ['town', 'bridge', 'river'],
        'ans1': ['You step into the main plaza of the town of Riverstone', 7, 'no_fight'],
        'ans2': ['Crossing the bridge you end up back where it all began,you decide to rest awhile before starting again', 0, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
     {
        # 7 - entering town 
        'question': f"As you walk in you notice an inn and a general shop. You ponder whither you have time to rest or shop or should you press on towards the mountain.Do you enter the {colored('inn', 'red')}, decide to {colored('shop', 'red')} or head towards the castle by the {colored('mountain', 'red')}",
        'answers': ['inn', 'shop', 'mountain'],
        'ans1': ['You step into the main plaza of the town of Riverstone', 7, 'no_fight'],
        'ans2': ['Crossing the bridge you end up back where it all began,you decide to rest awhile before starting again', 0, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
     {
        # 8 - inn
        'question': f"As you walk in you hear a table talking about a man escaping from the dragon castle not long ago. You are greeted by the innkeeper and offered a room for 20 gold. Do you {colored('rest', 'red')}, join the {colored('table', 'red')} to hear more or return to the {colored('town', 'red')} center.",
        'answers': ['rest', 'table', 'town'],
        'ans1': ['You all sleep well. Felling fully refreshed you step out into the town at dawn ready to continue', 7, 'no_fight'],
        'ans2': ['You sit down at the table to inquire about what you overheard', 9, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },
     {
        # 9 - table
        'question': f"The men all fall silent as you sit down. After reassuring them you mean no harm, you ask about this escape. An older man begins to tell you of a secret tunnel. ONe he is will to show you. For a price... 30 gold coins Do you {colored('pay', 'red')}, {colored('threaten', 'red')}  him to show you or return to the entrance of the {colored('inn', 'red')}.",
        'answers': ['rest', 'table', 'town'],
        'ans1': ['You all sleep well. Felling fully refreshed you step out into the town at dawn ready to continue', 7, 'no_fight'],
        'ans2': ['You sit down at the table to inquire about what you overheard', 9, 'no_fight'],
        'ans3': ['You head forwards', 3, 'no_fight']
    },



]