from english_words import get_english_words_set
from colorama import Back, Style


words = get_english_words_set(['gcide', 'web2'], alpha=True, lower=True)


def choose_word() -> str:
    word = words.pop()
    words.add(word)
    return word


def evaluate_guess(guess: str, answer: str) -> list[str]:
    """
    :param guess: the guess
    :param answer: the right answer
    :return: a list where the index corresponds to the position in the string and the value corresponds to the right
    colour
    """
    out = ['grey' for _ in range(len(answer))]

    # to deal with repeating letters, we must keep count
    used = {}
    for c in answer:
        used[c] = 0

    for i, c in enumerate(guess):
        if answer[i] == c:
            out[i] = 'green'
            used[c] += 1

    for i, c in enumerate(guess):
        if out[i] == 'green':  # ignore already processed letters
            continue

        if c in answer and used[c] < answer.count(c):
            out[i] = 'yellow'
            used[c] += 1

    return out


def print_evaluation(guess: str, evaluation: list[str]) -> None:
    """
    print the guess again but coloured
    :param guess: the guess
    :param evaluation: result of evaluate_guess
    """
    for i, c in enumerate(guess):
        if evaluation[i] == 'yellow':
            print(Back.YELLOW + c + Style.RESET_ALL, end='')
        elif evaluation[i] == 'green':
            print(Back.GREEN + c + Style.RESET_ALL, end='')
        else:
            print(c + Style.RESET_ALL, end='')
    print()


def legal_guess(guess: str, answer: str) -> bool:
    """
    a legal guess is one that is the right length and is a real word and is lower case
    :param guess: the guess
    :param answer: the right answer
    :return: true if guess is legal
    """
    return len(guess) == len(answer) and guess in words and guess.islower()


def game() -> None:
    """
    the main function to run the game
    """
    while True:
        print('starting new game...')
        won = False
        count = 0

        word = choose_word()
        print(f'the chosen word is {len(word)} characters long')

        while not won:
            guess = input('enter a guess: ')

            if guess == 'give up':
                print(f'the answer was: {word}')
                break

            if not legal_guess(guess, word):
                print(f'guess must be {len(word)} characters long and a real english word (some words are not in the '
                      f'games dictionary) and lower case')
            else:
                count += 1
                evaluation = evaluate_guess(guess, word)
                print_evaluation(guess, evaluation)
                if evaluation == ['green' for _ in range(len(word))]:
                    print(f'you win! and it only took you {count} tries')
                    won = True


if __name__ == '__main__':
    game()
