import random

print("Let's Get Start")
number_of_players = int(input("Enter the number of players (2-4): "))
players_list = list(range(1,number_of_players+1))
player_score = 0
global user_input
def roll_out():
    global random_number
    random_number = random.randrange(1, 7)
    print("You got", random_number)

# if player_score < 25:
# means the below code has to be exicute for all three players until the player_score get 25 or more than 25
while player_score <= 25:
    for i in players_list:
        print("Player ", i, "turn")
        user_input = input("You want to roll it(y/n): ")
        if user_input == 'y':
            roll_out()
            if random_number == 6:
                player_score = player_score + random_number
                print("play again")
                roll_out()
            else:
                player_score = player_score + random_number
                print("Total_score = ", player_score)



















