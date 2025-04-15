from random import randint

random_number = randint(1,100)
geuss_counter = 0

while True:
    
    player_number = int(input("Geuss a number between 1-100: "))
    geuss_counter += 1
    
    if player_number < 1 or player_number > 100:
        print("OUT OF BOUNDS!")
    elif random_number == player_number:
        print("You've geussed the correct number!")
        if geuss_counter == 1:
            print("It took you 1 guess.")
        else:
            print(f"It took you {geuss_counter} guesses.")
        break
    
    if geuss_counter == 1:
        if abs(random_number - player_number) <= 10:
            print("WARM!")
        elif abs(random_number - player_number) > 10:
            print("COLD!")
    else:
        if abs(random_number - previous_geuss) > abs(random_number - player_number):
            print("WARMER!")
        else:
            print("COLDER!")

    previous_geuss = player_number


    
  