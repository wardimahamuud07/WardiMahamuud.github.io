from time import sleep

#Game intro
print("=============================")
print("Welcome to Galactic Explorers")
print("=============================")
sleep(2)

print("You are a space captain, currently stranded in the vast milkyway with no way home.")
sleep(3)
print("In order to guide your crew back to your home planet, you must complete a number of questions.")
sleep(3)
print("These questions will allow you to reboot the engines that have failed and are keeping you stranded.")
sleep(3)
print("Before we get started, you need to choose a character to play as!")
sleep(1)

#Character Selection
print("Character 1 - 'Captain Alfred' ")
print("Character 2 - 'Captain Nate'   ")
print("Character 3 - 'Captain Lilly'  ")

character_choice = input("Choose your character choice: 1, 2 or 3: ")

if character_choice == "1":
   chosen_character = "Captain Alfred"
   print(f"{chosen_character} boards the command bridge, ready to begin the mission.....")
elif character_choice == "2":
    chosen_character = "Captain Nate"
    print(f"{chosen_character} boards the command bridge, ready to begin the mission....")
elif character_choice == "3":
    chosen_character = "Captain Lilly"
    print(f"{chosen_character} boards the command bridge, ready to begin the mission....")
else:
    print("Error, Invalid character selected.")

#Mission to repair flagged systems
nav_repaired = False
oxeygen_repaired = False
lighting_repaired = False

#Game looped, until all 3 systems have been repaired
while not (nav_repaired and oxeygen_repaired and lighting_repaired):

    #Repair navigation panel
    if not nav_repaired:
        print("The navagtion panel has been damaged")
        print("In order to repair it, you will need to answer a question")
        sleep(2)

        answer = int(input("What is the output of print(84+33)"))
        if answer == 117:
            print("Correct! - Navigation panel restored")
            nav_repaired = True
        else:
            print("Incorrect - Navigation panel remains inactive.")


    #Repair oxyegen system
    if not oxeygen_repaired:
        print("The oxyegen system has been damaged aswell")
        print("In order to repair it you will need to answer another question")
        sleep(2)

        answer = int(input("What is the output of print(7 * 4)"))
        if answer == 28:
            print("Correct! - Oxyegen system restored")
            oxeygen_repaired = True
        else:
            print("Incorrect - Oxyegen system remains inactive")


    #Repair lighting system
    if not lighting_repaired:
        print("The lighting system has also been damaged")
        print("In order to restore it, you must answer a final question")
        sleep(2)

        answer = input("What is the datat type for numbers in python?")
        if answer == "Integer":
            print("Correct! - Lighting system has been restored")
            lighting_repaired = True
        else:
            print("Incorrect - Lighting system remains inactive")

#End of the game
print("Well done! - All systems are now online, you are now ready to return home!")