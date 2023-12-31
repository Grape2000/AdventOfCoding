# Cube Conundrum

# colour = red, green, blue
# bag of cubes
# multiple games
# bag has: 12 red cubes, 13 green cubes, and 14 blue cubes
# output = sum of IDs of those games

##### part 1 ############# 

#open the text file  
#with open('Day2.txt', 'r') as f: 
  #read the text file into a list of lines 
#  lines = f.readlines() 
 
#create an empty dictionary 
#file_dict = {} 
 
#loop through the lines in the text file  
#for line in lines: 
  #split the line on ':' 
#  key, value = line.split(':') 
  #strip the whitespace 
#  key = key.strip() 
#  value = value.strip() 
#  #add the key, value pair to the dictionary 
#  file_dict[key] = value 
   
#print the dictionary 
#print(file_dict) 

#games = file_dict
#print(games)



#### solution:
# game_round(x,y,z,xt,yt,zt): 
# if: (x <= xt) AND (y <= yt) AND (z <= zt)
# every round has to be valid for a game to be right -> loop
# loop over each round and each game


# function: if: (x <= red) AND (y <= blue) AND (z <= green)
def game_round(blue, green,red, blue_total, green_total, red_total):
  if blue <= blue_total and green <= green_total and red <= red_total:
    return True
  else:
    return False

#game_round(2,4,6,5,5,10) -> True
#game_round(13, 12, 7, 12, 14, 8) -> False

# data structure to colour to adapt a number -> dictionary
# translate every round into a dictionary
round1 = {"blue":3, "red":4, "green":0}
round2 = {"blue":4, "red":1, "green":3}
round3 = {"blue":0, "red":0, "green":2}
round4 = {"blue":15, "red":0, "green":2}
maximum_values = {"blue":12, "green":13, "red":14}

game_round(round1["blue"], round1["green"], round1["red"], maximum_values["blue"], maximum_values["green"],maximum_values["red"])

# game1 is a list of rounds
# game is valid if every round is valid
game1 = [round1, round2, round3, round4]

def is_game_valid(game):
  is_valid = []
  for round in game:
    current_round = game_round(round["blue"], 
                               round["green"], 
                               round["red"], 
                               maximum_values["blue"], 
                               maximum_values["green"],
                               maximum_values["red"])
    is_valid.append(current_round)
  game_valid = all(is_valid) #function if all is valid
  return game_valid


# have data as a list of all games and every game as a dictionary with rounds
# translate data into usefull list with dictionary
# : seperates game ID from rounds
# ; seperates rounds in each game
# , seperates colours in each round


######### working solution #############

with open("Day2.txt", "r") as f:
    games = f.read().split("\n")


def read_game(game):
    result = []
    game = game.split(":")
    game_id = game[0].split()[1]
    shows = game[1].split(";")
    for i, show in enumerate(shows): #go throught list but know index and item -> returns pair 
        result.append({"blue": 0, "red": 0, "green": 0})
        for draw in show.split(","):
            count, color = draw.strip().split(" ")
            result[i][color] = int(count)
    return game_id, result

def is_allowed(game, max_allowed):
    for show in game:
        for color, count in show.items():
            if count > max_allowed[color]:
                return False
    return True

games[0]

max_allowed = {"blue": 14, "red": 12, "green": 13}
id_sum = 0
for game in games:
    game_id, game = read_game(game)
    if is_allowed(game, max_allowed):
        id_sum += int(game_id)

print(id_sum)


############ part 2 #################
with open("Day2.txt", "r") as f:
    games = f.read().split("\n")

for game in games:
    game_id, game = read_game(game)
    
game

def power(game):
    result = {"blue": 0, "red": 0, "green": 0}
    game = game.split(":")
    game_id = game[0].split()[1]
    shows = game[1].split(";")
    for i, show in enumerate(shows):
        for draw in show.split(","):
            count, color = draw.strip().split(" ")
            if result[color] < int(count):
                result[color] = int(count)
    return result["blue"] * result["red"] * result["green"]


total_power = 0
for game in games:
    game_power = power(game)
    total_power += game_power

print(total_power)