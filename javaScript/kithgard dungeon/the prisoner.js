// Free the prisoner, defeat the guard and grab the gem.

// Free Patrick from behind the "Weak Door".
hero.attack("Weak Door");
// Defeat the guard, named "Two".
hero.moveRight(3);
hero.moveDown();
hero.attack("Two");
hero.attack("Two");
// Get the gem.
hero.moveDown(2);