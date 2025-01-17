import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART_DICT = {
        1 : ["A","E","I", "O", "U", "L", "N", "R", "S", "T"],
        2 : ["D", "G"],
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"],
        8 : ["J", "X"],
        10: ["Q", "Z"]
    }

def draw_letters():    
    letter_pool_list = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool_list.append(letter)

    letter_bank = []
    for i in range(10):
        selection = random.choice(letter_pool_list)
        letter_bank.append(selection)
        letter_pool_list.remove(selection)

    return letter_bank

def uses_available_letters(word, letter_bank):
    letters_played = ""
    letter_bank_copy = letter_bank.copy()
    for letter in word:
        if letter in letter_bank_copy:
            letters_played += letter
            letter_bank_copy.remove(letter)
    played_letters_in_hand = (word == letters_played)
    return played_letters_in_hand



def score_word(word):  
    point_count = 0
    for letter in word.upper():
        for key, value in SCORE_CHART_DICT.items():
            if letter in SCORE_CHART_DICT[key]:
                point_count += key

    if len(word) in range(7, 11):
        point_count += 8
    
    return point_count

def get_highest_word_score(word_list):
    word_and_score_dict = {}
    max_score = 0
    max_word = []
    for word in word_list:
        score = score_word(word)
        word_and_score_dict[word] = score
        if score > max_score:
            max_score = score
            max_word = [word]
        elif score == max_score:
            max_word.append(word)

    if len(max_word) == 1:
        winning_word = max_word[0]
    elif len(max_word[0]) == len(max_word[1]):
        winning_word = max_word[0]
    elif len(max_word[0]) == 10:
        winning_word = max_word[0]
    elif len(max_word[1]) == 10:
        winning_word = max_word[1]
    elif len(max_word[0]) < len(max_word[1]):
        winning_word = max_word[0]
    else:
        winning_word = max_word[1]

    winning_tuple = (winning_word, word_and_score_dict[winning_word])

    return winning_tuple