# **TESTING**

You can return to the README.md file [here.](./README.md)

## PEP8 validation

All python files were passed through the CI validator at [pep8ci](https://pep8ci.herokuapp.com) and are all PEP8 compliant.

### Run.py

![run.py validation](./documentation/run_validation.png)

My run python file shoes no errors

### lists.py

![lists.py validation](./documentation/lists_validation.png)

My lists python file shoes no errors

### questions.py

![questions.py validation](./documentation/questions_validation.png)

My questions python file shoes no errors

### battle.py

![battle.py validation](./documentation/battle_validation.png)

My battle python file shoes no errors

## Error Handling 

The player has 10 unique input instances in this game. In this section I will document all of these, show their potential valid and expected inputs and how my approach to user input error has stopped any possible break in the application.

### input prompts

These are the 10 prompts the player will possibly see :

![Intro Prompt](./documentation/intro_prompt.png)

![Class Prompt](./documentation/class_prompt.png)

![Name Prompt](./documentation/class_prompt.png)

![Question Prompt](./documentation/question_prompt.png)

![Item Prompt](./documentation/item_prompt.png)

![Battle Prompt](./documentation/battle_prompt.png)

![Skill Prompt](./documentation/skill_prompt.png)

![Use Prompt](./documentation/use_prompt.png)

![Gameover Prompt](./documentation/gameover_prompt.png)

![Win Prompt](./documentation/win_game_prompt.png)


## Manual Testing  

Due to the step by step nature of the game and its branching paths most of the testing was done by brute force. Isolating parts of code to test wasn't nearly as useful as I have found with other projects as every decision in this game would carry on and had to carry over its changes into the next segment.

As it is a game I decided to try the game developers approach and try some QA testing by asking 2 friends on mine to run through different builds of the game and see if everything worked/ try purposefully break it. I am quite thankful I did in the end as one friend caught a bug where at one instance where you are supposed to give coins away everything worked fine but one later on in the game it didn't. This ended up being due to the order of a list of strings which I don't think I would have noticed myself.

## Bugs and issues

I am happy to report I had no notable bugs or real issues with this project other than one detailed above in [Manual Testing](#manual-testing). One of the only issues that grinded my progress to a halt was the fact that copying in standard python only creates a reference or a link to the original variable instead of its own instance. Thanks goes to my CI mentor Tim who dug me out of that whole straight away.

Other than that I feel that because my code was simple in structure due to my unfamiliarity with python, it did not leave a huge amount of room for app breaking bugs. I am sure there is much more efficient and cleaner looking ways in python to get the same results but the basic design behind the code structures one definite plus was it kept me away from any huge bugs or issues.

