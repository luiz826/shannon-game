def check_guess(guess: str, correct: str) -> bool:
    if guess != correct:  # if valid input, but not the correct letter
        return False
    # correct letter guessed
    return True


def check_is_valid_guess(guess: str) -> bool:
    if len(guess) > 1 or len(guess) == 0:
        return False
    return True


def get_guess(self, guess) -> str:
    return guess


available_chars = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
]
