from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n\n")
print("Name                  HP                                     MP")
print("                      _________________________              _______________")
print(bcolors.BOLD + "Hammad  "+
           "     460/460 |" + bcolors.OKGREEN + "████████                 " + bcolors.ENDC + "|   " +
                       "   65/65 |" + bcolors.OKBLUE + "███████████████" + bcolors.ENDC + "|")
print("                      _________________________              _______________")
print(bcolors.BOLD + "Valos   "+
           "     460/460 |" + bcolors.OKGREEN + "████████                 " + bcolors.ENDC + "|   " +
                       "   65/65 |" + bcolors.OKBLUE + "███████████████" + bcolors.ENDC + "|")
print("                      _________________________              _______________")
print(bcolors.BOLD + "Valos   "+
           "     460/460 |" + bcolors.OKGREEN + "████████                 " + bcolors.ENDC + "|   " +
                       "   65/65 |" + bcolors.OKBLUE + "███████████████" + bcolors.ENDC + "|")
print("\n\n")

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
hielixer = Item("Mega Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item" : potion, "quantity" : 15}, {"item" : hipotion, "quantity" : 5},
                {"item" : superpotion, "quantity" : 5}, {"item" : elixer, "quantity" : 5},
                {"item" : hielixer, "quantity" : 2}, {"item" : grenade, "quantity" : 5}]


# Instantiate People
player1 = Person(460, 65, 60, 35, player_spells, player_items)
enemy = Person(1200, 60, 45, 25, [], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attack" + bcolors.ENDC)
while running:
    print("##########################")
    player1.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player1.generate_damage()
        enemy.take_damage(dmg)

        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player1.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player1.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        current_mp = player1.get_mp()

        player1.reduce_mp(spell.cost)

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot Enough MP!" + bcolors.ENDC)
            continue

        if spell.type == "white":
            player1.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for" + str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + spell.name + " deals", str(magic_dmg), "points of damage." + bcolors.ENDC)

    elif index == 2:
        player1.choose_item()
        item_choice = int(input("Choose Item: ")) - 1

        if item_choice == -1:
            continue
        
        item = player1.items[item_choice]["item"]

        if player1.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "None left..." + bcolors.ENDC)
            continue

        player1.items[item_choice]["quantity"] -= 1


        if item.type == "potion":
            player1.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "elixer":
            player1.hp = player1.maxhp
            player1.mp = player1.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)

    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player1.get_hp()) + "/" + str(player1.get_maxhp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player1.get_mp()) + "/" + str(player1.get_maxmp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
        running = False