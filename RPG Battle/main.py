from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]


player1 = Person(460, 65, 60, 35, magic)
enemy = Person(1200, 60, 45, 25, magic)

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
        magic_dmg = player1.generate_spellDMG(magic_choice)

        spell = player1.get_spellName(magic_choice)
        cost = player1.get_spellMPcost(magic_choice)

        current_mp = player1.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot Enough MP!" + bcolors.ENDC)
            continue

        player1.reduce_mp(cost)
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