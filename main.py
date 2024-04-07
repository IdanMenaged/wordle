from english_words import get_english_words_set
from colorama import Back, Style


def choose_word() -> str:
    words = get_english_words_set(['gcide', 'web2'], alpha=True, lower=True)
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


if __name__ == '__main__':
    e = evaluate_guess('babes', 'abbey')
    print_evaluation('babes', e)
