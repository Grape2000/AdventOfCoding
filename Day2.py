# Cube Conundrum

# colour = red, green, blue
# bag of cubes = number unnown
# multiple games
# bag has: 12 red cubes, 13 green cubes, and 14 blue cubes
# output = sum of IDs of those games


##### part 1 ############# 

#open the text file  
with open('Day2.txt', 'r') as f: 
  #read the text file into a list of lines 
  lines = f.readlines() 
 
#create an empty dictionary 
file_dict = {} 
 
#loop through the lines in the text file  
for line in lines: 
  #split the line on ':' 
  key, value = line.split(':') 
  #strip the whitespace 
  key = key.strip() 
  value = value.strip() 
  #add the key, value pair to the dictionary 
  file_dict[key] = value 
   
#print the dictionary 
print(file_dict) 

games = file_dict

# loop
possible_bag = ""
options = ["1 blue", "2 blue", "3 blue", "4 blue", 
           "1 red", "2 red", "3 red", "4 red",
           "1 green", "2 green", "3 green", "4 green"]

for ID in games:
    for number in ID:
        if value == options:
            possible_bag += "Ok"
pos = possible_bag
print(pos)

# if Game ID has red <= 12
# if Game ID has green <= 13
# if Game ID has blue <= 14 
# add to possible 


# then sum amount of possible IDs
#IDsum = 0
#for sum in possible_bag:
#    IDsum += int(sum)
#print(IDsum)