print('''
@  *  .  . *       *    .        .        .   *    ..
 @. /\ *     ###     .      .        .            *
 @ /  \  *  #####   .     *      *        *    .
 ]/ [] \  ######### *    .  *       .  //    .  *   .
 / [][] \###\#|#/###   ..    *     .  //  *  .  ..  *
 |  __  | ###\|/###  *    *  ___o |==// .      *   *
 |  |!  |  # }|{  #         /\  \/  //|\
 |  ||  |    }|{    ejm97  / /        | \
                           ` `        '  '
''')
print('Welcome to Treasure Island.\nYour mission is to find the treasure')
print("You're at a cross road, Where do you want to go?")
cross_road = input("Type 'left' or 'right':\n ").lower()

if cross_road == 'left': # or 'Left'
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input('Type "wait" to wait for a boat. "Swim" to swim across.\n').lower()
    if lake == 'wait': #or 'Wait'
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        color = input("Red, yellow and blue. Which colour do you choose?\n").lower()
        if color == 'yellow':
            print('You win')
        elif color == 'red':
            print('Burned by fire. Game over')
        elif color == 'blue':
            print('Eaten by beasts. Game over')
        else:
            print('Game over')
    else:
        print('Attacked by trout. Game over')
else:
    print('Fall into a hole. Game over')