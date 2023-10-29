from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("BLizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cure", 18, 200, "white")

# Instantiate People
player1 = Person(460, 65, 60, 35, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 60, 45, 25, [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attack" + bcolors.ENDC)
while running:
    print("##########################")
    player1.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player1.generate_damage()
        enemy.take_damage(dmg)

        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player1.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        spell = player1.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        current_mp = player1.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot Enough MP!" + bcolors.ENDC)
            continue

        player1.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + spell + " deals", str(magic_dmg), "points of damage." + bcolors.ENDC)

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