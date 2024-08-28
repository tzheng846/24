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
generate messages for all operations in list format
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

'''
algorithum for two cards, produce list of length 6
'''
def two_card_algo(cards= example_card[:2]):
    div = []
    if(cards[0] != 0 and cards[1] != 0):
        div = [cards[0]/cards[1],cards[1]/cards[0]]
    results= [cards[0]+cards[1],cards[0]-cards[1],cards[1]-cards[0],cards[0]*cards[1]] + div
    return results

'''
algorithum for three cards, prints all possible solution to 24 with the given 3 cards
'''
def three_card_algo(cards= example_card[:3]):
    CARD_COMBINATIONS = [(0, 1),(0, 2),(1, 2)]
    solutions = []
    #for every combination of 2 cards
    for i in CARD_COMBINATIONS:
        #produce 2 card results and find index of 3rd card
        two_card_results = two_card_algo([cards[i[0]],cards[i[1]]])
        third_card_index = [x for x in (0,1,2) if x not in i][0]
        #for every results within 2 card results (6 results)
        for two_card_result_index in range(len(two_card_results)):
            #find new results with the new 3rd card (6 results) and generate msg for 2 card results using indexing
            third_card_results = two_card_algo([two_card_results[two_card_result_index], cards[third_card_index]])
            two_card_msg = msg_generator(cards[i[0]],cards[i[1]])[two_card_result_index]
            #if 24 is within third card results then find the index of the 24
            if(24 in third_card_results):
                for third_card_results_indicies in range(len(third_card_results)):
                    #generate msg using index of 3 card results that has 24
                    three_card_msg = msg_generator(two_card_results[two_card_result_index],cards[third_card_index])[third_card_results_indicies]
                    if(third_card_results[third_card_results_indicies] == 24):
                        #adds solution into solution list
                        solutions.append((two_card_msg,three_card_msg))
    for i in solutions:
        print(i)

'''
algorithum for four cards, prints all possible solution to 24 with the given 4 cards
'''
def four_card_algo(cards=example_card):
    #lists all combinations of 2 cards
    CARD_COMBINATIONS = list(combinations([0,1,2,3],2))
    solutions = []
    #for every combination of 2 cards
    for i in CARD_COMBINATIONS:
        two_card_results = two_card_algo([cards[i[0]],cards[i[1]]])
        third_card_index_list = [x for x in (0,1,2,3) if x not in i]
        #loop through index of two card results
        for two_card_result_index in range(len(two_card_results)):
            #loop through remaining combinations. Ex: first iteration - [2,3]
            for third_card_index in third_card_index_list:
                #generate results and msg
                three_card_results = two_card_algo([two_card_results[two_card_result_index],cards[third_card_index]])
                two_card_msg = msg_generator(cards[i[0]],cards[i[1]])[two_card_result_index]
                #use 4th number
                fourth_card_index = [x for x in (0,1,2,3) if x not in list(i)+ [third_card_index]][0]
                for fourth_number_index in range(len(three_card_results)):
                    fouth_card_results = two_card_algo([three_card_results[third_card_index],cards[fourth_card_index]])
                    three_card_msg = msg_generator(two_card_results[two_card_result_index],cards[third_card_index])[third_card_index]
                    if(24 in fouth_card_results):
                        for four_card_results_index in range(len(fouth_card_results)):
                            four_card_msg = msg_generator(three_card_results[third_card_index],cards[fourth_card_index])[four_card_results_index]
                            if(fouth_card_results[four_card_results_index]==24):
                                solutions.append((two_card_msg,three_card_msg,four_card_msg))
    if(not solutions):
        print("No Solution")
    else:
        print("Solutions:")
        for i in set(solutions):
            print(i)
    

cards =generate_cards()
print("Let's play 24! Here are your cards:",cards)
four_card_algo(cards)