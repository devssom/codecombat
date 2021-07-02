# Use what you've learned to defeat the ogres.
# Remember: it takes two attacks to defeat an ogre munchkin!
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
    else:
        hero.moveRight()