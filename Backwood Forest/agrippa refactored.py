def cleaveOrAttack(enemy):
    # If "cleave" is ready, cleave; otherwise, attack.
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            # Call the "cleaveOrAttack" function, defined above.
            cleaveOrAttack(enemy)