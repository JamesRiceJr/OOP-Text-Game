from room import Room
from character import Enemy
from character import Character
from character import Friend
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room('Dining Hall')
dining_hall.set_description("A large room with ornate golden decorations on each wall")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny floor.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Braiiiinnnnns")
dave.set_weakness("cheese")

laura = Friend("Laura", "Laura creates and maintains Raspberry Pi educational resources. Aside from computers, she loves cats, cakes, board games and making jam.")
laura.set_conversation("Sorry, did you somehow put me inside your game?")
laura.favorites = ["computer", "computers", "cats", "cat", "cake", "cakes", "board game", "board games"]

cheese = Item("cheese")
cheese.set_description("This is a wedge of cheese.")

roland = Enemy("Roland", "An evil cat.")
roland.set_weakness("tuna")

tuna = Item("tuna")

kitchen.set_character(laura)
dining_hall.set_character(dave)
ballroom.set_character(roland)
kitchen.set_item(cheese)

backpack = []

current_room = kitchen

game = True
wins = 0

while (game) & wins < 1:
  print("\n")
  current_room.get_details()
  inhabitant = current_room.get_character()
  room_item = current_room.get_item()
  if inhabitant is not None:
    inhabitant.describe()
  if room_item is not None:
    print("In the room you see a " + room_item.name + ".")
  command = input("> ")
  if command == "examine":
    print(room_item.get_description())
  if command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command) 
  elif command == "talk":
    inhabitant.talk()
  elif command == "fight":
    print("What will you fight with?")
    fight_with = input()
    if fight_with in backpack:
      if inhabitant.fight(fight_with) == False:
        print("Game Over")
        game = False
      else:
        print("You won the fight!")
        inhabitant = None
        wins += 1
    else:
      print("You don't have that item.")
  elif command == "bribe":
    print("How much of a bribe will you give?")
    bribe_amount = input()
    if inhabitant.bribe(bribe_amount):
      print("Whew! That was close, but better safe than sorry.")
      inhabitant = None
    else:
      print("Game Over")
      game = False
    
  elif command == "gift":
    print("What do you want to give?")
    gift = input()
    inhabitant.gift(gift)
    print('Laura says "I heard there is a hungry cat somewhere in here. Maybe this will help."' )
    print("Laura gave you an item: tuna.")
    backpack.append(tuna.name)
    
  elif (command == "pickup") & (room_item is not None):
    print("You picked up " + room_item.name + ".")
    backpack.append(room_item.name)
    room_item.pickup()
    current_room.item = None
  
  elif command == "backpack":
    print("You have in your backpack:")
    for i in backpack:
      print(i)
print("Congrats, you beat " + str(wins) + " enemies and won the game. Thanks for playing!")
