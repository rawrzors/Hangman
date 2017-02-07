from RandomWord import RandomWord
from Dictionary import Dictionary

class Hangman:
    word = ""
    current_word = list()
    difficulty = 1
    maxAttempts = 8
    currentAttempts = 0
    guesses = list()
    hints = list()
    current_hints = 0
    word_source = "api"

    def header(self, option = None):
        print("--------------")
        if option is None:
            print("Hangman")
        else:
            print("Hangman - "+option)
        print("--------------")

    def main_menu(self):
        self.header("Main Menu")
        print("1. Start")
        print("2. Settings")
        print("0. Exit")
        option = input("Select your option [1,2,0] ")
        return option

    def settings_menu(self):
        while True:
            self.header("Settings Menu")
            print("1. Difficulty")
            print("2. Max attempts")
            print("0. Exit")
            settings_option = input("Select your option [1,2,0] ")
            if settings_option == "1":
                self.difficulty_menu()
            elif settings_option == "2":
                self.max_attempts_menu()
            elif settings_option == "0":
                return
            else:
                print("Please select a valid option")

    def difficulty_menu(self):
        while True:
            self.header("Difficulty Menu")
            print("Current difficulty: " + format(self.difficulty))
            try:
                option = int(input("Set difficulty [1,2,3] or [0] to exit "))
                if option == 1:
                    self.difficulty = option
                    print("Difficulty set to "+ format(self.difficulty) + " - easy")
                    return
                elif option == 2:
                    self.difficulty = option
                    print("Difficulty set to " + format(self.difficulty) + " - medium")
                    return
                elif option == 3:
                    self.difficulty = option
                    print("Difficulty set to " + format(self.difficulty) + " - hard")
                    return
                elif option == 0:
                    return
                else:
                    print("Please select a valid option")
            except ValueError:
                print("Input must be a positive integer")

    def max_attempts_menu(self):
        self.header("Max attempts")
        print("Current max attempts: " + format(self.maxAttempts))
        while True:
            try:
                option = int(input("Set max attempts or [0] to exit "))
                if option == 0:
                    return
                elif option > 0:
                    self.maxAttempts = option
                    print("Set max attempts to "+ format(self.maxAttempts))
                    return
                else:
                    print("Input must be a positive integer")
            except ValueError:
                print("Input must be a positive integer")

    def start_game(self):
        print("Hangman game starting...")
        print("Settings - Difficulty: ["+format(self.difficulty)+"] Max attempts: ["+format(self.maxAttempts)+"]")
        self.word = self.get_word()
        self.hints = self.get_hints(self.word)
        self.current_word = list()
        self.guesses = list()
        self.current_hints = 0
        self.currentAttempts = 0
        self.update_word_progress()
        self.output_current_word()
        print("Press 0 at any time to exit and 1 for hint [{}] available".format(len(self.hints)))

        while True:
            self.output_guessed()
            guess = input("Attempt: [{}] out of [{}] Guess a letter: ".format(self.currentAttempts,self.maxAttempts))
            if guess.isalpha() and len(guess) == 1 and guess not in self.guesses:
                self.guesses.append(guess)
                result = self.word_check(guess)
                if(result):
                    print("Correct!")
                    self.output_current_word()
                    if(self.check_win()):
                        return 1;
                else:
                    print("Wrong.")
                    if(self.check_max_attempts()):
                        print("Max attempts reached - you ded")
                        print("Word was: "+self.word)
                        return 0;
                self.currentAttempts += 1
            elif guess == "1":
                print("Hint!")
                self.show_hint()
            elif guess == "0":
                print("Exiting...")
                return
            else:
                print("Error: Please guess a single letter that you have not guessed before.")

    def update_word_progress(self, indexes = {}, guess = ""):
        if len(self.current_word) == 0:
            for letter in self.word:
                self.current_word.append("_")
        else:
            for i in indexes:
                self.current_word[i] = guess

    def check_win(self):
        if set(self.word) == set(self.current_word):
            print("WINNER!")
            return True
        return False

    def check_max_attempts(self):
        if self.currentAttempts >= self.maxAttempts:
            return True
        return False

    def word_check(self, guess):
        if guess in self.word:
            indexes = self.find(self.word, guess)
            self.update_word_progress(indexes, guess)
            return True
        else:
            return False

    def get_hints(self, word):
        dict = Dictionary()
        word_info = dict.get_word_info(word)
        return dict.get_word_definition(word_info,word)

    def show_hint(self):
        if self.current_hints >= len(self.hints):
            print("You have already used up all your hints!")
            return False
        else:
            print(self.hints[self.current_hints])
            ++self.current_hints
            return True

    def output_current_word(self):
        print()
        print("###############################")
        for letter in self.current_word:
            print(" "+letter,end="")
        print()
        print("###############################")

    def output_guessed(self):
        if(len(self.guesses) > 0):
            guessString = ','.join(map(str, self.guesses))
            print("You have already guessed: "+guessString)

    def generate_word(self, method = 'local'):
        self.word = self.get_word()
        return self.word

    def get_word(self):

        if self.word_source == 'local':
            if self.difficulty == 1:
                return 'catcat'
            elif self.difficulty == 2:
                return 'tiger'
            elif self.difficulty == 3:
                return 'feline'
        elif self.word_source == 'api':
            random_word = RandomWord()
            word = random_word.get_random_word(5)
            return word

    def find(self, lst, a):
        result = []
        for i, x in enumerate(lst):
            if x == a:
                result.append(i)
        return result
