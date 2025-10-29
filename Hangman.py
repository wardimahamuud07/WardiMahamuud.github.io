import random
import time

STAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

right = 0
stage = 0

word = random.choice(words)
chars = list(word)

progress = []
for a in chars:
    progress.append("_")

def printout():
    conc = ""
    for a in progress:
        conc = conc + a
    print(conc)

def acknowledge(char):
    for a, b in enumerate(chars):
        if b is char:
            progress[a] = b
            global right
            right = right + 1

printout()


while stage < 6:
    if right == len(chars):
        print("You won!, the word was", word)
        break

    b = input()
    if b in chars:
        if not b in progress:
            acknowledge(b)
            printout()
    else:
        stage = stage + 1
        hangman = STAGES[stage].splitlines()
        for a in hangman:
            print(a)
            time.sleep(0.1)
        print("\n")
else:
    print("You lost!, the word was", word)