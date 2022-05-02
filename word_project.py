from word_class import game_word
import random

def GAME_TIME() :
    with open("words.txt") as word:
        word_list = word.read().splitlines()

    #This chooses a random word from the text file
    random_num = random.randint(0, len(word_list)-1)
    word_chosen = word_list[random_num]

    correct_letters = []
    guessed_letters = []
    lives = 7
    player_win = False



    my_word = game_word(word_chosen.lower(), correct_letters, guessed_letters)
    correct_letters = my_word.set_up()

    while lives > 0:
        print(*correct_letters, sep = ' ')
        #For debugging purposes, the line below reveals the word. 
        #print(word_chosen.lower())
        lives = my_word.guess(lives) 
        print(f'All of your guessed letters so far: {guessed_letters}')
        print(f'You have {lives} lives remaining.')
        my_word.win(player_win)
        if my_word.win(player_win) == True:
            print("Congratulation!!!! You have won!!!!")
            break
        if lives == 0:
            print("YOU HAVE RUN OUT OF LIVES. YOU LOSE LOSER")
            break
    
    again = input('Would you like to play again? type y/n ')
    if again == 'y':
        GAME_TIME()

GAME_TIME()