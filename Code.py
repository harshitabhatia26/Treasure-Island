print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

dir_1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' \n ")

if dir_1 == "left " :
  print("It's a room full of fire. Game Over.")
else: dir_2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
if dir_2 == "wait" :
  print("You enter a room of beasts. Game Over.")
else: dir_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
if dir_3 == "red" :
  print("You chose a door that doesn't exist")
elif dir_3 == "blue" :
  print("You found the treasure. You win!")
else: print("You fell into a hole. Game Over")
input("Press ENTER to exit")
