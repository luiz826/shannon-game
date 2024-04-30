import random
from typing import List

class ShannonGame:
    def __init__(self, sentences: List[str]) -> None:
        self.sentences = sentences

    def get_guess(self) -> str:
        return input("\n").lower()



    def send_response(self, resp) -> None:
        print(resp)
        pass

    @staticmethod
    def check_guess(guess: str, correct: str) -> bool:
        if (guess != correct): # if valid input, but not the correct letter
            return False
        # correct letter guessed
        return True
    
    @staticmethod
    def check_is_valid_guess(guess: str) -> bool:
        if len(guess) > 1 or len(guess) == 0:
            return False
        return True
    
    def game(self, sentence: str):
        """
        iterates through each letter in the sentence, checks against user prompted guess
        stores items in a dictionary
        :param sentence: random sentence selected to be guessed
        """

        # initializes empty guess string
        progress_string = ["_  "] * len(sentence)
        try_num = []
        
        print(f"This sentence contains {len(sentence)} letters. Start guessing! \n")
        print(" ".join(progress_string))

        for i, s in enumerate(sentence):
            guess_num = 0
            is_guess_correct = False
            guesses = [] # letters guessed

            while not is_guess_correct:
                guess = self.get_guess()
                is_a_valid_guess = self.check_is_valid_guess(guess)

                if not is_a_valid_guess:
                    print("Please enter one letter at a time. \n" )
                    self.send_response(f"Please, enter one letter at a time")
                else:
                    print(" " .join(progress_string) + " \n")
                    is_guess_correct = self.check_guess(guess=guess, correct=s)

                    if is_guess_correct:
                        try_num.append(guess_num + 1)
                        progress_string[i] = s
                        print("Good guess! \n" + ", ".join(map(str, try_num)))
                        print("  " .join(progress_string))
                        self.send_response(f"Good guess! you guessed correctly, with {guess_num + 1} tries.")
                    else:
                        if guess not in guesses:
                            guess_num += 1
                            guesses.append(guess)
                            print(f"Guess again! \nGuess count: {guess_num} \n")
                            self.send_response(f"Guess again, please! you tried {guess_num + 1} times until now.")
                        else:
                            self.send_response(f"You already guessed that! Try again, please!")
                            print("You already guessed that! Try again \n")
        
        assert try_num == sentence

        return try_num

    def play_game(self):
        table = {}
        for sentence in self.sentences:
            num_guesses, log = self.game(sentence)
            table[sentence] = num_guesses
            print(log)

        print(table)

ShannonGame(["banana"]).play_game()