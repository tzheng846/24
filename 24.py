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
def two_card_algo(cards= example_card[:2]):
    results= [cards[0]+cards[1],cards[0]-cards[1],cards[1]-cards[0],cards[0]*cards[1],cards[0]/cards[1],cards[1]/cards[0]]
    return results
def check_solution(results,cards):
    solution = []
    if(results[0]==24):
        solution.append("{}{}{}{}".format(cards[0]," + ",cards[1]," = 24"))
    if(results[1]==24):
        solution.append("{}{}{}{}".format(cards[0]," - ",cards[1]," = 24"))
    if(results[2]==24):
            solution.append("{}{}{}{}".format(cards[1]," - ",cards[0]," = 24"))
    if(results[3]==24):
            solution.append("{}{}{}{}".format(cards[0]," * ",cards[1]," = 24"))
    if(results[4]==24):
            solution.append("{}{}{}{}".format(cards[0]," / ",cards[1]," = 24"))
    if(results[5]==24):
            solution.append("{}{}{}{}".format(cards[1]," / ",cards[0]," = 24"))

    if(not solution):
        print("No Solution for " + str([cards[0],cards[1]]))
    return solution

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


def msg_generator(card1,card2):
     return ["{} + {} = {}".format(card1, card2,card1+card2),
                         "{} - {} = {}".format(card1, card2,card1-card2),
                         "{} - {} = {}".format(card2, card1,card2-card1),
                         "{} * {} = {}".format(card1, card2,card1*card2),
                         "{} / {} = {}".format(card1, card2,card1/card2),
                         "{} / {} = {}".format(card2, card1,card2/card1)]

three_card_algo(generate_cards())