from termcolor import colored
import random
import time
import os

from lists import party_list, monster_list, item_list


def battle_start(current_monster):

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
            self.attack = mon['attack']
            self.skills = mon['skills']

            self.stun = False

    player1 = Player(party_list[0])
    player2 = Player(party_list[1])
    player3 = Player(party_list[2])
    monster = Monster(monster_list[current_monster])

    party = [player1, player2, player3]

    def action_phase(player):
        action = input(f"Do you {colored('attack', 'red')}, use a {colored('skill', 'red')} or {colored('use', 'red')} an item?\n")

        if action == 'attack':
            os.system('clear')
            monster.hp = monster.hp - player.attack
            print(f"{player.name} did {player.attack} damage!\n\n")
        elif action == 'skill':
            skill = input(f"Do you want to use {colored('1', 'red')}) {player.skills[0]['name']} or {colored('2', 'red')}) {player.skills[1]['name']}\n")
            if skill == '1' and player.sp >= player.skills[0]['cost']:
                os.system('clear')
                player.sp = player.sp - player.skills[0]['cost']
                monster.hp = monster.hp - player.skills[0]['attack']
                if player.skills[0]['special'] is True:
                    monster.stun = stun()
                print(f"{player.name} did {player.skills[0]['attack']} damage!\n\n")
                if monster.stun is True:
                    print("You managed to stun your foe!\n")
                    monster.stun = True
                if player.skills[0]['attack'] == 0:
                    player.hp += 5
                    print('You healed yourself for 5HP!\n')
            elif skill == '2' and player.sp >= player.skills[1]['cost']:
                os.system('clear')
                player.sp = player.sp - player.skills[0]['cost']
                monster.hp = monster.hp - player.skills[1]['attack']
                if player.skills[1]['special'] is True:
                    monster.stun = stun()
                print(f"{player.name} did {player.skills[1]['attack']} damage!\n\n")
                if monster.stun is True:
                    print("You managed to stun your foe!\n")
                    monster.stun = True
                if player.skills[1]['attack'] == 0:
                    player.hp += 5
                    print('You healed yourself for 5HP!\n')
        elif action == 'use':
            os.system('clear')
            potion = input(f"Do you want to use a {colored('1', 'red')}) Health Potion or a {colored('2', 'red')}) Skill Potion\n")

            if potion == '1' and item_list['health_potion'] > 0:
                item_list['health_potion'] -= 1
                player.hp += 10
                os.system('clear')
                print(f"{player.name} restored 10HP!")
            elif potion == '2' and item_list['skill_potion'] > 0:
                item_list['skill_potion'] -= 1
                player.sp += 10
                os.system('clear')
                print(f"{player.name} restored 10 skill points!")
            else:
                os.system('clear')
                print('Invalid option. Try again!\n')
                action_phase(player)
        else:
            os.system('clear')
            print('Invalid option. Try again!\n')
            action_phase(player)

    def monster_phase():
        if monster.hp <= 0:
            print("The monster is defeated!\n\n")
            return

        if monster.stun is True:
            print('The beast is stunned and misses its turn!')
            monster.stun = False
            time.sleep(2)
        else:
            target_player = random.randint(0, 2)
            mon_attack = random.randint(0, 100)
            if mon_attack < 70:
                party[target_player].hp = party[target_player].hp - monster.attack
                print(f"The beast does {monster.attack} damage to {party[target_player].name}!\n\n")
                time.sleep(2)
            else:
                party[target_player].hp = party[target_player].hp - monster.skills[0]['attack']
                print(f"The beast uses {monster.skills[0]['name']} and does {monster.skills[0]['attack']} damage to {party[target_player].name}!\n\n")
                time.sleep(2)

    def update_stats(player, player_obj):
        player['health_points'] = player_obj.hp
        player['skill_points'] = player_obj.sp

    print(f"A battle with the {monster_list[current_monster]['name']} begins!\n\n")

    while (player1.hp > 0 and player2.hp > 0 and player3.hp > 0) and monster.hp > 0:
        print(f"{player_stats(party_list[0])}")
        action_phase(player1)
        print(f"{player_stats(party_list[1])}")
        action_phase(player2)
        print(f"{player_stats(party_list[2])}")
        action_phase(player3)
        monster_phase()
        update_stats(party_list[0], player1)
        update_stats(party_list[1], player2)
        update_stats(party_list[2], player3)

    print(f"Congratulations you have slain the {monster.name}!\n\n")
    if current_monster == 3:
        time.sleep(2)
        print(  
            f"{colored('CONGRATULATIONS', 'white', 'on_red')}"
            "you have saved the realm and finished your quest!"
            "Thanks for playing!")
        input('Press enter to close the game!')
        quit()  
    time.sleep(2)
    return


def stun():
    stun_chance = random.randint(0, 2)
    if stun_chance == 0:
        return False
    else:
        return True


def player_stats(p):
    print(
        (f"{p['name']} -- {p['player_name']}'s Turn!\n"
            f"HP: {p['health_points']}\nSkill Points: {p['skill_points']}\n"
            f"Skills:\n{colored(p['skills'][0]['name'], 'green')} "
            f"- {p['skills'][0]['dis']}\n"
            f"{colored(p['skills'][1]['name'], 'green')} "
            f"- {p['skills'][1]['dis']}\n\n"))
