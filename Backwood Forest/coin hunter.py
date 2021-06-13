# To make the training more interesting Senick poisoned you.
# While you aren't moving the poison is harmless.

# This function should check if a coin is closer than 20m.
def isCoinClose(coin):
    # Find the distance to the `coin`.
    distance = hero.distanceTo(coin)
    # If the distance is less than 20: 
    if distance < 20:
        # Return True
        return True
    # Else:
    else:
        # Return False
        return False
    pass

while True:
    item = hero.findNearestItem()
    if item:
        # If isCoinClose(item) returns true:
        if isCoinClose(item):
            hero.moveXY(item.pos.x, item.pos.y)