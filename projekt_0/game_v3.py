"""Guess the number game
The computer makes its own guess, and guesses the number itself
"""

import numpy as np


def optimal_predict(number:int=1) -> int:
    """We guess the number considering whether the number is greater or less than the number we need.

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    count = 0
    left_border = 1
    right_border = 100
    while True:
        count += 1        
        # guess the average value from the range of possible
        predict_number = (left_border+right_border) // 2  
        if number == predict_number:
            break # exit the loop if we guessed right   
        # decrease the range of values by half
        elif number > predict_number:
            left_border = predict_number + 1
        elif number < predict_number:
            right_border = predict_number - 1
    return count

def score_game(optimal_predict) -> int:
    """For how many attempts on average for 1000 approaches does our algorithm guess
    
    Args:
        optimal_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    
    count_ls = []
    np.random.seed(1) # fixing the RANDOM SEED so that the experiment is reproducible
    random_array = np.random.randint(1, 101, size=(1000)) # guess a list of numbers 
    
    for number in random_array:
        count_ls.append(optimal_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number on average for : {score} attempts')
    return score
   
   
    
if __name__ == '__main__':
    # RUN
    score_game(optimal_predict)
