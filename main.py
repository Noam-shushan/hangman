from hangman import *

"""
Author: noam shushan
Email: noam8shu@gmail.com
"""

def main():
    print(data.HANGMAN_ASCII_ART)
    print('Number of guesses allowed is', data.MAX_TRIES)
    file_path = input('Please enter a file path\n-> ')
    index_secret_word = int(input('Please enter a position to word in the file\n-> '))

    secret_word = choose_word(file_path, index_secret_word)
    if secret_word is None:
        print('ERROR: the position you enter is out of the range in the file')
        return

    print('Let’s start!')
    print_hangman(0)

    old_letters_guessed = []
    curr_num_correct_guesses = 0
    count_fail_tries = 0

    while count_fail_tries < data.MAX_TRIES:
        letter_guessed = input('Guess a letter: ').lower()
        prev_num_correct_guesses = curr_num_correct_guesses

        if not check_valid_input(letter_guessed):
            print('X')
            continue

        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            is_win, curr_num_correct_guesses = check_win(secret_word, old_letters_guessed)
            if not is_win:
                show_hidden_word(secret_word, old_letters_guessed)
                # Checks whether correct letters have been added to the guess list
                if prev_num_correct_guesses == curr_num_correct_guesses:
                    count_fail_tries += 1
                    print(':(')
                    print_hangman(count_fail_tries)
            else:
                print('Win!')
                break

    if count_fail_tries == data.MAX_TRIES:
        print('Lose!')


if __name__ == '__main__':
    main()



