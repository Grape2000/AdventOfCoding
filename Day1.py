# given: code words as a string (1abc24f)
# output: first and last digit of string to form a two digit number and then add them together (sum)



### how to put data input into a list and split lines???
# split into new lines -> /n and put it into a list
#text = open("Day1.txt","r").read().strip()
#data = text.split("\n")
#line = "".join(data)
#exampel = [line]
#print(exampel)   



###### below works

#line = "1abc2"
# extract all numbers
#list = ["1","2","3","4","5","6","7","8","9"]
#numbers = ""
#i = 0

#for i in line:
#    if i in list:
#        numbers += i
#print(numbers)

        
# find first [0:] and last digit [-1:] (e.g. 1 and 5) and out them together
#digit = numbers[0] + numbers[-1]
#print(digit)

# sum all two digit numbers





#################### solution from simon ############################
# part 1
from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "Day1.txt"

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

lines_list = readFile(filename_path)
print(lines_list)

digits = ["0","1","2","3","4","5","6","7","8","9"]
temp = []
result = []
for line in lines_list:
    for char in line:
        if char in digits:
            temp.append(char)
    result.append(temp[0] + temp[-1])
    temp = []

print(result)

digit_sum = 0
for digit in result:
    digit_sum += int(digit)
print(digit_sum)

###############################################

