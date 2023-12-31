# Scratchcards

# part 1#
winning = {}
have = {}
with open("Day4.txt", "r") as cards:
    for line in cards.readlines():
        card_id = line.split(":")[0].split()[1]
        winning[card_id] = set(line.split(":")[1].split("|")[0].split())
        have[card_id] = set(line.split(":")[1].split("|")[1].split())
total_points = 0
for card in winning.keys():
    intersect = winning[card].intersection(have[card])
    if len(intersect) > 0:
        total_points += 2**(len(intersect) - 1)

print(total_points)




# part 2 #
winning = {}
have = {}
multiplicity = {}
with open("Day4.txt", "r") as cards:
    for line in cards.readlines():
        card_id = int(line.split(":")[0].split()[1])
        winning[card_id] = set(line.split(":")[1].split("|")[0].split())
        have[card_id] = set(line.split(":")[1].split("|")[1].split())
        multiplicity[card_id] = 1
total_points = 0
for card in winning.keys():
    intersect = winning[card].intersection(have[card])
    for m in range(multiplicity[card]):
        for i, _ in enumerate(intersect):
            if card + i + 1 not in multiplicity:
                continue
            multiplicity[card + i + 1] += 1
    # print(card, multiplicity)
    total_points += multiplicity[card]

print(total_points)