from Hangman import Hangman

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