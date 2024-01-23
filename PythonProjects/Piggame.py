import random

print("Let's Get Start")
number_of_players = int(input("Enter the number of players (2-4): "))
players_list = list(range(1,number_of_players+1))
player_score = [0,0,0]
i = 0
score = player_score[i]
global user_input
def roll_out():
    global random_number
    random_number = random.randrange(1, 7)
    print("You got", random_number)

while player_score[i] <= 25:
    for i in players_list:
        print("Player ", i, "turn")
        user_input = input("You want to roll it(y/n): ")
        if user_input == 'y':
            roll_out()
            # if random_number == 6:
            player_score[i] = player_score[i] + random_number
            #     print("play again")
            #     roll_out()
            # else:
            #     player_score[i] = player_score[i] + random_number
            print("Total_score = ", player_score[i])
            if player_score[i] >= 25:
                print("Winner is player ", i)




















