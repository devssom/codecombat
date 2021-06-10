while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # If there is an enemy, attack it!
        hero.attack(enemy)
        pass