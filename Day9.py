# Day 9 Mirage Maintenance

# make new sequence from the difference at each step
# if thats not all zeroes repeat process
# when zero add one next number (with same step)
# add together all last numbers


# given: lists of numbers with pattern
# output: sum of next number predicted by pattern

# data
#from unittest import result


#def read_input(path):
#    sequences = []
#    with open(path, 'r') as f:
#        for line in f.readlines():
#            sequences.append([int(x) for x in line.strip().split()])

#    return sequences

#seq = read_input("Day9.txt")




#############################################
def read_input(path):
    sequences = []
    with open(path, 'r') as f:
        for line in f.readlines():
            sequences.append([int(x) for x in line.strip().split()])

    return sequences
seq = read_input("Day9.txt")
def pairwise_diff(x):
    return [x[i+1] - x[i] for i in range(len(x)-1)]
def add_next(x):
    diff = pairwise_diff(x)
    # print(diff)
    if all([d == 0 for d in diff]):
        return 0
    else:
        return diff[-1] + add_next(diff)
    
def predict_next(x):
    return x[-1] + add_next(x)

def solve(seq):
    result = 0
    for s in seq:
        result += predict_next(s)
    return result
predict_next(seq[2])

solve(seq)

seq = read_input("Day9.txt")
solve(seq)


i = 0
print(seq[i])
w = add_next(seq[i])

print(w)