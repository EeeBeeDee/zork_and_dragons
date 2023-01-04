from termcolor import colored
import random
import os

from lists import party_list, monster_list
# from run import item_screen


def battle_start():

    class Player:
        def __init__(self, char):
            self.name = char['player_name']
            self.hp = char['health_points']
            self.sp = char['skill_points']
            self.attack = char['attack']
            self.skills = char['skills']

    class Monster:
        def __init__(self, mon):
            self.name = mon['name']
            self.hp = mon['health_points']
            self.sp = mon['skill_points']
            self.attack = mon['attack']

            self.stun = False

    player1 = Player(party_list[0])
    player2 = Player(party_list[1])
    player3 = Player(party_list[2])
    monster = Monster(monster_list[0])

    while (player1.hp > 0 and player2.hp > 0 and player3.hp > 0) and monster.hp > 0:
        print(f"Remember type {colored('item', 'green')} on your first players turn to see your stats!")
        print(f"\n{player1.name}'s turn\n\n")
        action_p1 = input(f"Do you {colored('attack', 'red')}, use a {colored('skill', 'red')} or {colored('use', 'red')} an item?\n")

        if action_p1 == 'attack':
            os.system('clear')
            monster.hp = monster.hp - player1.attack
            print(f"{player1.name} did {player1.attack} damage!\n\n")
        elif action_p1 == 'skill':
            p1_skill = input(f"Do you want to use {colored('1', 'red')}) {player1.skills[0]['name']} or {colored('2', 'red')}) {player1.skills[1]['name']}\n")
            if p1_skill == '1':
                monster.hp = monster.hp - player1.skills[0]['attack']
                if player1.skills[0]['special'] is True:
                    monster.stun = stun()
                print(f"{player1.name} did {player1.skills[0]['attack']} damage!\n\n")
                if monster.stun is True:
                    print("You managed to stun your foe!")
                if player1.skills[0]['attack'] == 0:
                    player1.hp += 5
                    print('You healed yourself for 5HP!')
            elif p1_skill == '2':
                monster.hp = monster.hp - player1.skills[1]['attack']
                if player1.skills[1]['special'] is True:
                    monster.stun = stun()
                print(f"{player1.name} did {player1.skills[1]['attack']} damage!\n\n")
                if monster.stun is True:
                    print("You managed to stun your foe!")
                if player1.skills[1]['attack'] == 0:
                    player1.hp += 5
                    print('You healed yourself for 5HP!')


def stun():
    stun_chance = random.randint(0, 2)
    if stun_chance == 0:
        return False
    else:
        return True
