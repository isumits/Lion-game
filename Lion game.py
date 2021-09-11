#hide and seek
from random import randint
print('Lion game')
hide = True
score = 0
while hide:
    Lion_door = randint(1,3)
    print('Three doors ahead ---> ')
    print('A Lion behind one ')
    print('Lion cahnges its position randomly')
    print('dont get caught by lion and score a point')
    print('which door  you want to open')
    door = input('1,2,0r 3?')
    door_num = int(door)
    if door_num == Lion_door:
        print('Its Lion!')
        hide = False
    else:
        print(' Lion is not here')
        print('You can enter the next room .')
        score = score + 1
print('Run away')
print('Game over ! You scored ', score)
