# Use a loop to attack the skeleton.
# Its blunt sword hardly does any damage, but it has huge knockback.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)