class Hangman:
    word = ""
    current_word = list()
    difficulty = 1
    maxAttempts = 8
    currentAttempts = 0
    guesses = list()

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
        word = self.generate_word()
        self.current_word = list()
        self.guesses = list()
        self.currentAttempts = 0
        self.update_word_progress()
        self.output_current_word()

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
                        return 0;
                self.currentAttempts += 1
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


    def game_menu(self):
        self.header()

    def generate_word(self, method = 'local'):
        self.word = self.get_word()
        return self.word

    def get_word(self):
        if self.difficulty == 1:
            return 'catcat'
        elif self.difficulty == 2:
            return 'tiger'
        elif self.difficulty == 3:
            return 'feline'

    def find(self, lst, a):
        result = []
        for i, x in enumerate(lst):
            if x == a:
                result.append(i)
        return result