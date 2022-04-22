"""
Programming Assignment 4. Task 6.
A game.
"""
import my_own_game
from my_own_game import SpaceOrRoom, Character, Friend, Enemy, Item

your_bedroom = SpaceOrRoom('Bedroom')
your_bedroom.set_description('Here you have a sofa, your desk and a closet.')

hall = SpaceOrRoom('Hall')
hall.set_description('A broad hall from where you can enter many other rooms.')

svitlytsia = SpaceOrRoom('Svitlytsia')
svitlytsia.set_description('A room for recess, where many of the residents of the dormitory\
 get together to watch TV or play board games.')

elevator = SpaceOrRoom('Elevator')
elevator.set_description('A decent-sized elevator without a mirror\
 which is very upsetting.')

corridor = SpaceOrRoom('Corridor')
corridor.set_description('A corridor leading from the elevator to\
 the kitchen')

kitchen = SpaceOrRoom('Kitchen')
kitchen.set_description('A tiny room that nonetheless has enough place\
 for every cooking utensil you may think of.')

entrance_hall = SpaceOrRoom('Entrance hall')
entrance_hall.set_description("This is the hall right before the main exit.\
 You're really close to escaping the dormitory!")

freedom = SpaceOrRoom("Street")
freedom.set_description("Hooray! You're in the street! You've escaped the dormitory!")

your_bedroom.link_room(hall, "west")
hall.link_room(your_bedroom, "east")
hall.link_room(svitlytsia, "west")
svitlytsia.link_room(hall, "east")
svitlytsia.link_room(elevator, "south")
elevator.link_room(svitlytsia, "north")
elevator.link_room(corridor, "west")
corridor.link_room(elevator, "east")
corridor.link_room(kitchen, "south")
kitchen.link_room(corridor, "north")
kitchen.link_room(entrance_hall, "west")
entrance_hall.link_room(kitchen, "east")
entrance_hall.link_room(freedom, "south")
freedom.link_room(entrance_hall, "north")


lilia = Friend("Lilia", "Just an ordinary dormitory resident")
lilia.set_conversation("Hey! How are you? :)")
hall.set_character(lilia)

andriy = Enemy("Andriy", "Andriy is your lazy neighbour who blatantly refuses\
 to clean the hall and the svitlytsia even though it's his turn to do so.\
 And since you, by your very nature, cannot tolerate such negligence, you\
 absolutely cannot leave the dormitory without once again admonishing him and\
 shoving the cleaning schedule in his face.")
andriy.set_conversation("I'm sorry I cannot talk right now")
andriy.set_weakness("Cleaning Schedule")
svitlytsia.set_character(andriy)

platon = Enemy("Platon", "Platon is a very cute little boy of 6, however\
 he is as naughty as one can be. Most of the time he's either making people's\
 car alarm systems go off because he's playing football in the parking lot, or\
 he's running headlong across the halls while pushing fire alarm buttons.\
 However, his absolute favorite pastime is going up and down the 7-story\
 building by pressing all the buttons in the elevator, thus not letting\
 other people use it.")
platon.set_conversation("Do you have games on your phone?")
platon.set_weakness("Chocolate Bar")
elevator.set_character(platon)

pascal = Friend("Pascal", "Pascal is a friendly volunteer who comes by every week\
 to bring some humanitarian aid to the dormitory.")
pascal.set_conversation("You doing fine, dear?")
corridor.set_character(pascal)

grandma_zoya = Enemy("Grandma Zoya", "This is a very lovely and kind old woman\
 whom you befriended while getting registered in the dormitory. She's been\
 constantly giving you treats and home-made food, which was utterly delicious.\
 However, because of that you've started gaining weight and you've decided it's\
 better to avoid her for a while not to offend her by refusing to eat all the cakes.")
grandma_zoya.set_conversation("Oh here you are! Just give my new pie a taste!")
grandma_zoya.set_weakness("Crossword")
kitchen.set_character(grandma_zoya)

omar = Enemy("Omar", "This is a security guard who smiles excessivley at you every time\
 you meet him. He's not creepy, just a bit too friendly...the guy must heve become really\
 desperate looking for a girlfriend.")
omar.set_conversation("Hallo, wie geht es dir")
omar.set_weakness("ring")
entrance_hall.set_character(omar)

chocolate_bar = Item("Chocolate Bar")
chocolate_bar.set_description("A Milka Oreo chocolate bar")
kitchen.set_item(chocolate_bar)

cookie = Item("Cookie")
cookie.set_description("Just a sesame cookie")
hall.set_item(cookie)

crossword = Item("Crossword")
crossword.set_description("A magazine with crossword puzzles")
svitlytsia.set_item(crossword)

ring = Item("ring")
ring.set_description("A ring that looks suspiciously similar to an engagement ring")
your_bedroom.set_item(ring)

cleaning_schedule = Item("Cleaning Schedule")
cleaning_schedule.set_description("A schedule written and agreed upon collectively by\
 all residents of this floor.")
entrance_hall.set_item(cleaning_schedule)

current_room = your_bedroom
backpack = []
intro = "Hey! You have been placed in the dormitory for fugitives in Germany.\
 Here you've met a lot of your fellow Ukrainians but also German social workers\
, volunteers, security guards and others. You've developed friendly relations with\
 all of them, but for some reason you still feel like avoiding speaking to some of them.\
 In this game you'll have to travel the rooms to collect different objects and figure out\
 which ones will be a suitable tool to distract or ward off those who you do not want to meet for\
 now hehehe. Here's how to win the game: you have to ward off or distract everyone you do not want\
 to meet, and then go out of the dormitory by exiting through the main entrance. You\
 will also meet people whom you consider friends - there is no need to ward them off.\
 Good luck!"
print(intro)

warded_off = False

while warded_off is False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()
    
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        if current_room != entrance_hall:
            current_room = current_room.move(command)
        else:
            if command != "south":
                current_room = current_room.move(command)
            else:
                if omar.defeats == 0:
                    print("You cannot escape the dormitory without warding off the security guard!")
                
                else:
                    if omar.get_warded_off() != 4:
                        print("You cannot escape the dormitory without warding off everyone you intended to!")
                    else:
                        current_room = current_room.move(command)
                        print("Yay! You've escaped the dormitory!")
                        break


    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "ward off":
        if inhabitant is not None:
            # Ward off the inhabitant, if there is one.
            # Note however that you cannot fight friends.
            if not isinstance(inhabitant, Friend):
                print("What do you want to ward off this person with?")
                ward_off_with = input()

                # Do I have this item?
                if ward_off_with in backpack:

                    if inhabitant.ward_off(ward_off_with) is True:
                        # What happens if you win?
                        print("Hooray, you distraced or warded off that person!")
                        current_room.character = None
                        if inhabitant.get_warded_off() == 4:
                            print("Congratulations, you have warded off or avoided everyone you wanted to!")
                            # warded_off = True
                    else:
                        print("Oh, dear, you failed at warding off that person!")
                        print("That's the end of the game")
                        warded_off = True
                else:
                    print("You don't have a " + ward_off_with)
            else:
                print("You cannot ward off your friends!")
        else:
            print("There is no one to ward off here")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name()+ " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
                