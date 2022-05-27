"""
Autor: Elizeu Ferreira
5 Prove: Adventure Game

"""

print("ENTER CAPITAL LETTERS AND COME HAVE JOY")

answer = input("Would you like to play a adventure game?(YES/NOT) ")
if answer == "YES":
   print()
   print("Let's play and have fun!")
if answer == "NOT":
   print("Have a nice day!") 
   exit()
else:
   print("\nWELCOME TO THE ADVENTURE GAME: ")

  # Adventure
   answer = input("Which of these items would you choose to walk in the forest, in case you had lost? (MATCH/FLASHLIGHT) ")
if answer == "MATCH":
   print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.")
   answer = input("Do you want to RUN, or HIDE behind a tree? ")
   if answer == "RUN":
      print("Run fast for the bear not to eat you.")
      print("WIN THE GAME")
   if answer == "HIDE":
      print("You will be swallowed by the Bear.")
      print("GAME OVER!")
if answer == "FLASHLIGHT":
   print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
   print()
   answer = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
if answer == "FOLLOW":
   print("You found your way out of the forest and were not swallowed by the Bear.")
   print("WIN THE GAME")
if answer == "LOOK":
   print("You will be swallowed by the Bear.")
   print("SORRY, GAME OVER!!!")
