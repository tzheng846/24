import random
from itertools import combinations

example_card = [12, 2, 1, 6]

'''
generates random 4 numbers from 1 to 13
'''
def generate_cards():
    all_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    cards =[]
    for i in range(4):
        cards.append(int(random.choice(all_cards)))
    return cards
'''
displays numbers as cards- 11 is J, 12 is Q, 13 is K
'''
def show_cards(cards):
    dct = {11:"J",12:"Q",13:"K"}
    for i in range(len(cards)):
        if cards[i] in dct.keys():
            cards[i] = dct[cards[i]]
    return cards

'''
applies basic functions to list of 4 numbers and saves the 6 results
indexs:
0 - add
1 - subtract a-b
2 - subtract b-a
3 - multiply
4 - divide a/b
5 - divide b/a
'''
def msg_generator(card1,card2):
    div = []
    if(card1 != 0 and card2!= 0):
        div = ["{} / {} = {}".format(card1, card2,card1/card2),
               "{} / {} = {}".format(card2, card1,card2/card1)]
    return ["{} + {} = {}".format(card1, card2,card1+card2),
                         "{} - {} = {}".format(card1, card2,card1-card2),
                         "{} - {} = {}".format(card2, card1,card2-card1),
                         "{} * {} = {}".format(card1, card2,card1*card2)]+div


def two_card_algo(cards= example_card[:2]):
    div = []
    if(cards[0] != 0 and cards[1] != 0):
        div = [cards[0]/cards[1],cards[1]/cards[0]]
    results= [cards[0]+cards[1],cards[0]-cards[1],cards[1]-cards[0],cards[0]*cards[1]] + div
    return results

def three_card_algo(cards=example_card[:3]):
    CARD_COMBINATIONS = [(0, 1),(0, 2),(1, 2)]

    solutions = []
    for i in CARD_COMBINATIONS:
        two_card = two_card_algo([cards[i[0]],cards[i[1]]])
        third_card_index = [x for x in (0,1,2) if x not in i][0]
        operation_tracker = 0
        operation_msg = msg_generator(cards[i[0]],cards[i[1]])
        #for each new number generated from two_cards. Ex: [14, 10, -10, 24, 6.0, 0.16666666666666666]
        for new_number_index in range(len(two_card)):
            three_card = two_card_algo([two_card[new_number_index],cards[third_card_index]])
            if(24 in three_card):
                for i in range(len(three_card)):
                    if(three_card[i] == 24):
                        temp_solutions = []
                        #appends how the new two_card number was obtained
                        temp_solutions.append(operation_msg[operation_tracker])
                        #appends how the three_card number was obtained
                        temp_solutions.append(msg_generator(two_card[new_number_index],cards[third_card_index])[i])
                        solutions.append(tuple(temp_solutions))
            #update operation
            operation_tracker+=1
    for i in solutions:
        print(i)

def four_card_algo(cards=example_card):
    CARD_COMBINATIONS = list(combinations([0,1,2,3],2))
    solutions = []
    for i in CARD_COMBINATIONS:
        two_card_results = two_card_algo([cards[i[0]],cards[i[1]]])
        third_card_index = [x for x in (0,1,2,3) if x not in i]

        two_card_operation_tracker = 0
        two_card_operation_msg = msg_generator(cards[i[0]],cards[i[1]])
        test = []

        #loop through index of two card results
        for new_number_index in range(len(two_card_results)):
            #loop through remaining combinations. Ex: first iteration - [2,3]
            for third_card in third_card_index:
                #generate results and msg
                three_card_results = two_card_algo([two_card_results[new_number_index],cards[third_card]])
                three_card_msg = msg_generator(two_card_results[new_number_index],cards[third_card])
                three_card_dictionary = {k:v for (k,v) in zip(three_card_results,three_card_msg)}
                #use 4th number
                fourth_card_index = [x for x in (0,1,2,3) if x not in list(i)+ [third_card]][0]
                for fourth_number_index in range(len(three_card_dictionary.keys())):
                    fouth_card_results = two_card_algo([list(three_card_dictionary.keys())[fourth_number_index],cards[fourth_card_index]])
                    fouth_card_msg = msg_generator(list(three_card_dictionary.keys())[fourth_number_index],cards[fourth_card_index])
                    if(24 in fouth_card_results):
                        for i in range(len(fouth_card_results)):
                            if(fouth_card_results[i] == 24):
                                temp_solutions = []
                                #appends how the new two_card number was obtained
                                temp_solutions.append(two_card_operation_msg[two_card_operation_tracker])

four_card_algo()