class game_word:
    def __init__(self, word, correct_let, guessed_let):
        self.word = word
        self.correct_let = correct_let
        self.guessed_let = guessed_let
        print('Hello! Welcome to the game. You have been assigned a random word. time to start guessing letters!')



    def set_up(self):
        for i in range(len(self.word)):
            self.correct_let.append('_')
        return self.correct_let
    
    def guess(self, lives):
        self.lives = lives
        in_word = False
        end = False
        player_guess = input('What letter would you like to guess? ').lower()
        
        try:
            int_check = int(player_guess)
            if isinstance(int_check, int) == True:
                print("Hmmmmm seems like you put in a number. That is not allowed.\n So as punishment, I am subtracting the number you entered from your lives. Let's see what you have left...")
                lives = lives - int(player_guess)
                end = True
                return lives
        except:
            pass


        finally:
            if end == True:
                return lives
            for i in range(len(self.word)):
                if self.word[i] == player_guess:
                    self.correct_let[i] = player_guess
                    in_word = True
            if player_guess not in self.guessed_let and in_word == False:
                print(f'Sorry! {player_guess} was not in your chosen word. Try again!')
                lives -= 1
                self.guessed_let.append(player_guess)
            elif player_guess in self.guessed_let and in_word == False:
                print("Looks like you have already guessed that letter. Try again!")
            return lives



    def win(self, win):
        if '_' not in self.correct_let:
            win = True
            return win
