##### Day 7 

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VALUES = {card: alphabet[score] for score, card in enumerate(CARDS[::-1])}
def count_cards(hand):
    return {card: hand.count(card) for card in CARDS}

def order_hands(hands, deck_length=13):
    buckets = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    for hand in hands:
        breakdown = count_cards(hand)
        # Five of a kind, where all five cards have the same label
        if len(set(hand)) == 1:
            buckets[7].append(hand)
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if max(breakdown.values()) == 4:
            buckets[6].append(hand)
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        if sorted(breakdown.values()) == [0]*11 + [2, 3]:
            buckets[5].append(hand)
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        if sorted(breakdown.values()) == [0]*10 + [1, 1, 3]:
            buckets[4].append(hand)
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        if sorted(breakdown.values()) == [0]*10 + [1, 2, 2]:
            buckets[3].append(hand)
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        if sorted(breakdown.values()) == [0]*9 + [1, 1, 1, 2]:
            buckets[2].append(hand)
        # High card, where all cards' labels are distinct: 23456
        if len(set(hand)) == 5:
            buckets[1].append(hand)
    return buckets

def translate_hand(hand):
    return "".join([str(VALUES[card]) for card in hand])

def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key=seq.__getitem__)

def break_tie(hands):
    translated = [translate_hand(hand) for hand in hands]
    order = argsort(translated)
    return [hands[i] for i in order]

def final_order(buckets):
    final = []
    for priority in range(1, 8):
        bucket = buckets[priority]
        sorted = break_tie(bucket)
        final.extend(sorted)
    return final
sorted

hands = {
'32T3K': 765,
'T55J5': 684,
'KK677': 28,
'KTJJT': 220,
'QQQJA': 483,
}

buckets = order_hands(hands.keys())
final = final_order(buckets)
winnings = 0
for rank, hand in enumerate(final):
    winnings += hands[hand] * (rank + 1)
winnings

hands = {}
with open("Day7.txt", "r") as f:
    for line in f.readlines():
        hand, bid = line.split()
        hands[hand] = int(bid)
buckets = order_hands(hands.keys())
final = final_order(buckets)
winnings = 0
for rank, hand in enumerate(final):
    winnings += hands[hand] * (rank + 1)
winnings


print(winnings)





############ part 2 ########
CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VALUES = {card: alphabet[score] for score, card in enumerate(CARDS[::-1])}
def count_cards(hand):
    return {card: hand.count(card) for card in CARDS}

def order_hands(hands, deck_length=13):
    buckets = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    for hand in hands:
        breakdown = count_cards(hand)
        if "J" not in hand:
            # Five of a kind, where all five cards have the same label
            if len(set(hand)) == 1:
                buckets[7].append(hand)
            # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
            if max(breakdown.values()) == 4:
                buckets[6].append(hand)
            # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
            if sorted(breakdown.values()) == [0]*11 + [2, 3]:
                buckets[5].append(hand)
            # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
            if sorted(breakdown.values()) == [0]*10 + [1, 1, 3]:
                buckets[4].append(hand)
            # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
            if sorted(breakdown.values()) == [0]*10 + [1, 2, 2]:
                buckets[3].append(hand)
            # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
            if sorted(breakdown.values()) == [0]*9 + [1, 1, 1, 2]:
                buckets[2].append(hand)
            # High card, where all cards' labels are distinct: 23456
            if len(set(hand)) == 5:
                buckets[1].append(hand)
        else:
            jhand = hand.replace("J", "")
            breakdown = count_cards(hand)
            breakdown = sorted(breakdown.values())
            if len(jhand) < 2: #JJJJX or JJJJJ
                buckets[7].append(hand)
            elif len(jhand) == 2:
                if len(set(jhand)) == 1: #JJJXX
                    buckets[7].append(hand)
                else: #JJJXY
                    buckets[6].append(hand)
            elif len(jhand) == 3: 
                if len(set(jhand)) == 1: #JJXXX
                    buckets[7].append(hand)
                elif len(set(jhand)) == 2: #JJXXY
                    buckets[6].append(hand)
                else: #JJXYZ
                    buckets[4].append(hand)
            elif len(jhand) == 4:
                if breakdown[-1] == 4: #JXXXX
                    buckets[7].append(hand)
                elif breakdown[-1] == 3: #JXXXY
                    buckets[6].append(hand)
                elif breakdown[-1] == 2: #JXX??
                    if breakdown[-2] == 2: #JXXYY
                        buckets[5].append(hand)
                    else: #JXXYZ
                        buckets[4].append(hand)
                else: #JXYZW
                    buckets[2].append(hand)
            else:
                print("ERROR", hand)
    return buckets
hands = {
'32T3K': 765,
'T55J5': 684,
'KK677': 28,
'KTJJT': 220,
'QQQJA': 483,
}
buckets = order_hands(hands.keys())
final = final_order(buckets)
winnings = 0
for rank, hand in enumerate(final):
    winnings += hands[hand] * (rank + 1)
winnings


hands = {}
with open("Day7.txt", "r") as f:
    for line in f.readlines():
        hand, bid = line.split()
        hands[hand] = int(bid)
buckets = order_hands(hands.keys())
final = final_order(buckets)
winnings = 0
for rank, hand in enumerate(final):
    winnings += hands[hand] * (rank + 1)
winnings


print(winnings)