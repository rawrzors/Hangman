class Hangman:
    word = ""
    currentWord = ""
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
                hangman.difficulty_menu()
            elif settings_option == "2":
                hangman.max_attempts_menu()
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
        self.update_word_progress()
        self.output_current_word()

        while True:
            guess = input("Guess a letter: ")
            self.output_guessed()
            if guess.isalpha() and len(guess) == 1:
                self.guesses.append(guess)
                self.word_check(guess)
            else:
                print("Please guess a letter")

    #
    def update_word_progress(self):
        if self.currentWord == "":
            for letter in self.word:
                self.currentWord += "_"

    def word_check(self, guess):
        return

    def output_current_word(self):
        print()
        print("###############################")
        for letter in self.currentWord:
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
            return 'cat'
        elif self.difficulty == 2:
            return 'tiger'
        elif self.difficulty == 3:
            return 'feline'

hangman = Hangman()

hangman.header()
input("Press enter to begin: ")

while True:
    option = hangman.main_menu()
    if option == '1': #gamestart
        hangman.start_game()
    elif option == '2': #settings
        settings_option = hangman.settings_menu()
    elif option == '0': #exit
        print("Bye!")
        break
    else: #invalid option
        print("Invalid option selected")