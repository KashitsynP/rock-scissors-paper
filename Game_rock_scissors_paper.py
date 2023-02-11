choise = int(input("1 - камень, 2 - ножницы, 3 - бумага: "))
import random
rand_n = random.randrange(1, 4, 1)
if rand_n == 1:
    print("У компьютера: 1 - камень")
elif rand_n == 2:
    print("У компьютера: 2 - ножницы")
else: 
    print("У компьютера: 3 - бумага")

if choise == 1:
    if rand_n == 2:
        print("You win")
    elif rand_n == 3:
        print("You lose")
    else:
        print("Drawn")
elif choise == 2:
    if rand_n == 3:
        print("You win")
    elif rand_n == 1:
        print("You lose")
    else:
        print("Drawn")
elif choise == 3:
    if rand_n == 1:
        print("You win")
    elif rand_n == 2:
        print("You lose")
    else:
        print("Drawn")
else:
    print("Error: incorrect number")
