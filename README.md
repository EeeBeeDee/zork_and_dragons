# **ZORK AND DRAGONS**

Zork and dragons is a text based adventure RPG game which literally wears its two biggest influences on its sleeves. Those being [Zork](https://en.wikipedia.org/wiki/Zork) a text based adventure game from the late 70s and the table top game dungeons & dragons.

Made up of two main areas of gameplay. A choose your next step question based system for progression and a turn based battle system. Trying to emulate some of my own favorite games I have tried to incorporate decisions that can lead to avoidance of combat while still advancing. 

The live site is available at [Zork and Dragons](https://zork-and-dragons.herokuapp.com/)

# Features

## Intro and tutorial

![Intro screen](./documentation/intro_screen.png)

The intro screen provides a brief explanation and tutorial for the game. Using the python library "colored" I convey that all valid responses will have their text colour as red. 

## Character select screen 

![Character Select Screen](./documentation/character_select.png)

The screen directly after the intro screen which allows you to pick your parties composition. As a nod to D&D and games like final fantasy its up to you if you go for the usual choice of nice and balanced or try beat the game with 3 archers!

## Adventure section

![Question Screen](./documentation/question_screen.png)

Here is the main portion of the game. Where all your questing decisions are made and progress happens. At the top will always be what effect your previous choice has had. Directly underneath will be the next part of the adventure which will present you with 3 different choices or paths highlighted with red text.

## Battle system

![Battle screen](./documentation/battle_screen.png)

Once a battle is entered this is the first screen you will see.
It displays all the info for each character as they take their turn going in the order of selection. 

Every character has the choice of using their normal attack, using 1 of their 2 skills or using a potion on themselves.

After all three player characters have taken their turns, whatever monster they are fighting will then attack.

Who dealt the attack, who received and how much damage was done is always displayed after each action. (As seen below)

![Attack display](./documentation/attack_state.png)

## Item Screen

![Item Screen](./documentation/intro_screen.png)

This screen is activated by typing item at any stage during your adventure that is outside of battle. It displays your current inventory and your parties current stats and abilities

# Future expansion

- Save System -- A save system would allow not only for people to step away but allow the games length to increase dramatically as it is constrained now by how long someone could stay playing in one sitting. A generated password system could work well which saved the current question players stats and names. Using a copy and paste-able piece of hex code that when inserted generated the lists I use now like party list and item list. 

- Experience System -- A standard leveling up system that allows your party to increase its stats. It could be done in a few easy enough ways I feel. 

    * A standard stat increase every level. so for example every time you level up you increase your attack by 2.
    * An incremental system where the percentage your stats grow by increase as your level gets higher. Easily implemented in one way by using the actual level variable your character will have and adding or multiplying into the stat increase
    * A system based off class where knights might get more health upon level up where archers get more attack.
    
- More Stats -- I would love to add more stats in to vary combat more. Two examples I can think of are: 

    * A defense stat that multiple the attackers damage by a number < 1 to create a scenario where less damage is done the higher the defense is.
    * A speed or dexterity stat to determine the order in which every character involved in battle takes their turn.
- Build Your Own Adventure -- One of the original ideas I had for this project and one that influenced the way I built it was a game where you could create the questions, monsters and classes for the party. The way all questions are based of off a list of objects which all have the same keys, I could implement a build your own adventure mode using the game here as an example people could enter in all their own stories and monsters. I found this one in particular to be outside on my own capabilities at this time.


# Technologies

[Heroku](https://heroku.com) - Used to deploy app to the web

[python](https://python.com) - App written in Python version 3.10.6

I also used multiple python libraries in this apps creation:

- random -- was used to create the 50% chance of the stun mechanic working 
- colored -- allowed me to highlight useable answers and draw attention to important words and phrases
- os -- allowed me to simulate the clear command to remove previous questions and player turns from terminal
- time -- used to create a pause after certain attacks to create dramatic effect
- copy -- used deepcopy to create full copies from my class_list list.

# Deployment

Details on deployment can be found inv the [DEPLOYMENT](./DEPLOYMENT.md) markdown file

Click this [link](https://zork-and-dragons.herokuapp.com/) to view the live heroku hosted application

# Testing

All testing and validation can be found in the [TESTING](./TESTING.md) markdown file.

# Acknowledgements

