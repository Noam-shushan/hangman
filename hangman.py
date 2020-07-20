import data
import re


def check_valid_input(letter_guessed):
    """
    Check if it is a valid letter
    :param letter_guessed: The letter the user guessed
    :type: letter_guessed: str
    :return: True if it is one letter only and if the character is a letter else False
    :rtype: bool
    """
    return len(letter_guessed) <= 1 and letter_guessed.isalpha()


def check_repeated_guess(letter_guessed, old_letters_guessed):
    """
    Checks if the letter is already guessed
    :param letter_guessed: The letter the user guessed
    :type: letter_guessed: str
    :param old_letters_guessed: list of the letters the user guessed
    :type: old_letters_guessed: list
    :return: True if letter_guessed not guessed already else False
    :rtype: bool
    """
    return old_letters_guessed.count(letter_guessed) <= 1


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Checks whether the letter has been guessed already,
    if so, prints a reminder to the user that he has already guessed that letter
    :param letter_guessed: The letter the user guessed
    :type: letter_guessed: str
    :param old_letters_guessed: list of the letters the user guessed
    :type: old_letters_guessed: list
    :return: True if the letter_guessed was successfully added to old_letters_guessed else False
    :rtype: bool
    """
    old_letters_guessed.append(letter_guessed)
    if check_repeated_guess(letter_guessed, old_letters_guessed):
        return True

    old_letters_guessed.pop()
    old_letters_guessed.sort()  # sort the letters to get them by the order
    # take every letter and add to her '->' (except from the last letter) and join everything to a string
    print(''.join(list(map(lambda letter: letter + '->', old_letters_guessed)))[:-2])
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Displays the letters from the old_letters_guessed list that are in the secret_word in their respective positions,
     and the rest of the letters in the string (which the user has not yet guessed) as underscores.
    :param secret_word: The word a user has to guess
    :type: secret_word: str
    :param old_letters_guessed: list of the letters the user guessed
    :type: old_letters_guessed: list
    :return: None
    """
    missing_letters = '_'*len(secret_word)  # number of underscores as the number of letters
    for i in old_letters_guessed:
        # gets the indexes of each letter of the secret word un our guess list
        indexes = [match.start() for match in re.finditer(i, secret_word)]

        for j in indexes:
            # insert the relevant letters instead of underscores
            missing_letters = missing_letters[:j]+i+missing_letters[j+1:]
    print(missing_letters)


def check_win(secret_word, old_letters_guessed):
    """
    Verify if all the letters that make up the secret word are included in the list of letters the user guessed.
     Otherwise, the function returns false
     To know whether correct letters were added to the guess list,
     the function also returns the number of correct letters at the moment
    :param secret_word: The word a user has to guess
    :type: secret_word: str
    :param old_letters_guessed: list of the letters the user guessed
    :type old_letters_guessed: list
    :return: a tuple of 2 items 1) True if the user guess every letter correct else False\
    2) the number of correct letters at the moment
    :rtype: tuple(bool, int)
    """
    # selects letters that appear in the secret word
    appearing_letters = set((filter(lambda letter: letter in secret_word, old_letters_guessed)))
    non_repeated_letters = set(secret_word)
    return appearing_letters == non_repeated_letters, len(appearing_letters)


def choose_word(file_path, index):
    """
    Opens a text file and returns the secret word that the user selected from the file
    :param file_path: a path to the file
    :type file_path: str
    :param index: location of random word from the file
    :type: index: int
    :return: the word that the user peek from the file
    :rtype: str
    """
    with open(file_path, 'r') as f:
        words = f.read().split()  # get an list of words spored by spaces
    if index > len(words):
        return None
    return words[index-1]  # return index-1 to allow the user select a indexed word from 1


def print_hangman(num_of_tries):
    """
    Displays the hangman figure according to the number of user tries
    :param num_of_tries: the number of tries the user guessed
    :type num_of_tries: int
    :return: None
    """
    print(data.HANGMAN_PHOTOS[num_of_tries])
