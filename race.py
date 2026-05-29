#jamal


# Initial Conditions
import random
def race():
        finish_line = 50  #Finish Line
        tortoise_pos = 0  #Starting Position
        hare_pos = 0		 #Starting Position
        is_hare_asleep = False #Hare starts Awake

# The Simulation Loop
        while tortoise_pos < finish_line and hare_pos < finish_line:
            move_tort =random.randint(1,3)
            if move_tort == 1:
                tortoise_pos=tortoise_pos +1
                print(f" Tortoise posoition is {tortoise_pos} meters")
            elif move_tort == 2:
                tortoise_pos=tortoise_pos +2
                print(f" Tortoise posoition is {tortoise_pos} meters")
            elif move_tort == 3:
                tortoise_pos=tortoise_pos +3
                print(f" Tortoise posoition is {tortoise_pos} meters")





            sleep_hare = random.randint(1,10)
            if sleep_hare <= 3:
                is_hare_asleep = True
                print("Hare is asleep")
            elif sleep_hare >= 4:
                is_hare_asleep =False
            if is_hare_asleep == False:


                move_hare= random.randint(1,10)
                if move_hare == 1:
                    hare_pos = hare_pos +1
                    print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 2:
                        hare_pos = hare_pos +2
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 3:
                        hare_pos = hare_pos +3
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 4:
                        hare_pos = hare_pos +4
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 5:
                        hare_pos = hare_pos +5
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 6:
                        hare_pos = hare_pos +6
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 7:
                        hare_pos = hare_pos +7
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 8:
                        hare_pos = hare_pos +8
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 9:
                        hare_pos = hare_pos +9
                        print(f" Hare's posoition is {hare_pos} meters")
                elif move_hare == 10:
                        hare_pos = hare_pos +10
                        print(f" Hare's posoition is {hare_pos} meters")


            if tortoise_pos >= finish_line:

                    print(" turlte wins")
                    break
            elif hare_pos >= finish_line:
                print("hare")
                break


race()
