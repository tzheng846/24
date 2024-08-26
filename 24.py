import random

def generate_cards():
    all_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    cards =[]
    for i in range(4):
        cards.append(int(random.choice(all_cards)))
    return cards
def show_cards(cards):
    dct = {11:"J",12:"Q",13:"K"}
    for i in range(len(cards)):
        if cards[i] in dct.keys():
            cards[i] = dct[cards[i]]
    return cards

def apply_augment(num1,num2):
    return [num1+num2,num1-num2,num2-num1,num1*num2,num1/num2,num2/num1,]

def find_combo():
    #DSF
    cards = generate_cards()
    for i in range(1,4):
        new_cards = apply_augment(cards[0],cards[i])
        print(cards)
        print(new_cards)

find_combo()