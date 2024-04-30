import random
from typing import List

class ShannonGame:
    def __init__(self, sentences: List[str]) -> None:
        self.sentences = sentences

    def get_guess(self) -> str:
        return input("Caractere? ").lower()

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
        
        progress_string = ["_"] * len(sentence)
        try_num = []
        
        print(f"Essa frase possui {len(sentence)} letras. Comece a escolher caractere! \n")
        print("".join(progress_string))

        for i, s in enumerate(sentence):
            guess_num = 0
            is_guess_correct = False
            guesses = [] # letters guessed

            while not is_guess_correct:
                guess = self.get_guess()
                is_a_valid_guess = self.check_is_valid_guess(guess)

                if not is_a_valid_guess:
                    print("Por favor, uma letra por vez. \n" )
                    self.send_response(f"Por favor, uma letra por vez")
                else:
                    print("Frase a ser adivinhada: ", end="")
                    print("" .join(progress_string) + " \n")
                    is_guess_correct = self.check_guess(guess=guess, correct=s)

                    if is_guess_correct:
                        try_num.append(guess_num + 1)
                        progress_string[i] = s
                        print("Acertou! \n" + ",".join(map(str, try_num)))
                        print("Frase a ser adivinhada: ", end="")
                        print("" .join(progress_string))
                        self.send_response(f"Boa tentativa! você escolheu correto com {guess_num + 1} tentativas.")
                    else:
                        if guess not in guesses:
                            guess_num += 1
                            guesses.append(guess)
                            print(f"Tente novamente! \nContador de tentativas: {guess_num} \n")
                            self.send_response(f"Tente novamente, por favor! Você tentou {guess_num} vezes até agora.")

                            print("Caracteres usados até agora: " + ", ".join(guesses) + "\n")
                        else:
                            self.send_response(f"Você já tentou essa, tente outro!")
                            print("Você já tentou essa, tente outro! \n")

        # assert try_num == sentence

        return try_num

    def play_game(self):
        table = {}
        for sentence in self.sentences:
            num_guesses = self.game(sentence)
            table[sentence] = num_guesses
            print(num_guesses)

        print(table)

ShannonGame(["banana"]).play_game()