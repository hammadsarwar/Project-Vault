from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]


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

        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)

    print("Enemy attacks for", enemy_dmg, "Player HP:", player1.get_hp())
    print("Hello")