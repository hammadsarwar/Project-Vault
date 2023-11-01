from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("BLizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cure", 18, 200, "white")

# Create some Item
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item" : potion, "quantity" : 15}, {"item" : hipotion, "quantity" : 5},
                {"item" : superpotion, "quantity" : 5}, {"item" : elixer, "quantity" : 5},
                {"item" : hielixer, "quantity" : 2}, {"item" : grenade, "quantity" : 5}]


# Instantiate People
player1 = Person("Hammad:", 3260, 100, 60, 35, player_spells, player_items)
player2 = Person("Valos :", 4160, 100, 60, 35, player_spells, player_items)
player3 = Person("Cook  :", 3089, 100, 60, 35, player_spells, player_items)
enemy = Person("Nigga🥷  :", 12000, 120, 245, 25, [], [])

players = [player1, player2, player3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attack" + bcolors.ENDC)
while running:
    print("########################")

    print("\n\n")
    print("Name                   HP                                  MP")
    for player in players:
        player.stats()

    print("\n")

    enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)

            print("You attacked for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg()

            current_mp = player.get_mp()

            player.reduce_mp(spell.cost)

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot Enough MP!" + bcolors.ENDC)
                continue

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for" + str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " deals", str(magic_dmg), "points of damage." + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                continue
        
            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1


            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp

                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    target = random.randrange(0, 3) # It will select random player index
    enemy_dmg = enemy.generate_damage()
    players[target].take_damage(enemy_dmg)  # Feed it here as an index to damage any random player

    print("Enemy attacks for", enemy_dmg, "points of damage.")

    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
        running = False