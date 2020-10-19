import eel


def choose_word(file_path, index):
    temp = ()
    file = open(file_path, "rt")
    data = file.read()
    words = data.split()
    words = list(dict.fromkeys(words))
    temp = (len(words), words[index - 1])
    return temp


def check_win(secret_word, old_letters_guessed):
    count = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            count += 1
    if len(secret_word) == count:
        return True
    else:
        return False


def show_hidden_words(secret_word, old_letters_guessed):
    hidden_word = []

    for letter in secret_word:
        if letter not in old_letters_guessed:
            hidden_word.append(" _ ")
        else:
            hidden_word.append(letter)

    return hidden_word


@eel.expose
def main_screen(file_path, index):
    selected_word = choose_word(file_path, index)
    secret_word = selected_word[1]
    return secret_word


@eel.expose
def game_screen(secret_word, old_letters_guessed, number_guess):
    letters_list = list(old_letters_guessed)
    letter_guessed = letters_list[-1]
    is_win = check_win(secret_word, old_letters_guessed)
    if not is_win:
        hidden_word = show_hidden_words(secret_word, old_letters_guessed)
        if letter_guessed in secret_word:
            return " ".join(hidden_word)
        else:
            return number_guess + 1
    else:
        return "YOU WON!"


eel.init('web')
eel.start('index.html', size=(1300, 570), port=0)  # python will select free ephemeral ports.
