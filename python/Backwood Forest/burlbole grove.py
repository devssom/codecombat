# Don't attack the burls!
# Functions can return a value.
# When a function is called, it will be equal to the value the function returns.

def shouldAttack(target):
    # return False if no `target`
    if target == False:
        return False
    # return False if target.type == "burl"
    elif target.type == "burl":
        return False
    # Otherwise, return True
    else: 
        return True

while True:
    enemy = hero.findNearestEnemy()
    # Here we use shouldAttack() to decide if we should attack!
    # heroShouldAttack will be assigned the same value that shouldAttack() returns!
    heroShouldAttack = shouldAttack(enemy)
    if heroShouldAttack:
        hero.attack(enemy)