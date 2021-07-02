# Big ogres can't see you in the forest.
# Attack only the small ogres in the forest.
# Collect coins and gems only.
# Don't leave the forest and don't eat/drink anything.

while True:
    # Find the nearest enemy.
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # Attack it only if its type is "thrower" or "munchkin".
    if enemy and distance < 20:
        if enemy.type == "thrower" or "munchkin":
            hero.attack(enemy)
    # Find the nearest item.
        item = hero.findNearestItem()
    # Collect it only if its type is "gem" or "coin".
    if item.type == "gem" or item.type== "coin":
        hero.moveXY(item.pos.x, item.pos.y)