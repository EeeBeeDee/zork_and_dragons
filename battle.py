from termcolor import colored
import random
import os

from lists import party_list, monster_list
from run import item_screen


class Player:
    def __init__(self, char):
        self.name = char['player_name']
        self.hp = char['health_points']
        self.sp = char['skill_points']
        self.attack = char['attack']


class Monster:
    def __init__(self, mon):
        self.name = mon['name']
        self.hp = mon['health_points']
        self.sp = mon['skill_points']
        self.attack = mon['attack']


def battle_start():
    player1 = Player(party_list[0])
    player2 = Player(party_list[1])
    player3 = Player(party_list[2])
    monster = Player(monster_list[0])

    while (player1.hp > 0 and player2.hp > 0 and player3.hp > 0) and monster.hp > 0:
        print(f"Remember type {colored('item', 'green')} on your first players turn to see your stats!")
        print(f"\n{player1.name}'s turn\n\n")
        action_p1 = input(f"Do you {colored('attack', 'red')}, use a {colored('skill', 'red')} or {colored('use', 'red')} an item?")
        if action_p1 == 'attack':
            os.system('clear')
            monster.hp = monster.hp - player1.attack
