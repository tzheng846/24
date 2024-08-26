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
        for i in two_card:
            three_card = two_card_algo([i,cards[third_card_index]])
            print(three_card)
        
three_card_algo()