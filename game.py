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

        return table

import numpy as np

def calc_upper_bound(table):

    count_probs = {}
    len_table = 0
    
    for guesses in table:
        len_table += 1
        if guesses not in count_probs.keys():
            count_probs[guesses] = 1
        else:
            count_probs[guesses] += 1
    
    upper_entropy = 0
    
    for k, v in count_probs.items():
        upper_entropy += (v / len_table) * np.log2(len_table / v)

    return upper_entropy

def calc_lower_bound(table):
    
    len_table = 0
    
    max_guesses = max(table)
    count_probs = {k: 0 for k in range(1, max_guesses + 1)}

    for guesses in table:
        len_table += 1
        count_probs[guesses] += 1
    
    lower_entropy = 0

    for n in range(1, max_guesses + 1):
        if n == max_guesses:
             p_1 = count_probs[n] / len_table
             lower_entropy += n * (p_1) * np.log2(n)
             # print(n * (p_1) * np.log2(n))
        else:
            p_1 = count_probs[n] / len_table
            p_2 = count_probs[n + 1] / len_table
            lower_entropy += n * (p_1 - p_2) * np.log2(n)
            # print(n * (p_1 - p_2) * np.log2(n))
    
    return lower_entropy



# table_guess = ShannonGame(["the broken v"]).play_game()
table_guess = [2,1,1,1,11,3,2,5,1,1,1,15]
upper_bound = calc_upper_bound(table_guess)
lower_bound = calc_lower_bound(table_guess)
mean_bound = (upper_bound + lower_bound) / 2

print(f"Upper bound: {upper_bound}")
print(f"Lower bound: {lower_bound}")
print(f"Entropy: {mean_bound}")


"""
Você vai jogar o jogo de shannon. 

Você precisa descobrir todos os caracteres de uma frase cujo alfabeto são as 26 letras do alfabeto minúsculas mais o caractere de espaço, logo, 27 caracteres ao todo.

Você só pode sugerir uma letra por resposta.

Você não pode repetir chutes já feitos.

Uma vez que você acertou uma letra, deve prever o próximo caractere com base no conhecimento dos caracteres anteriores. Além disso, você pode sugerir letras chutadas em tentativas anteriores, pois a cada acerto, a lista de letras já chutadas por você é reiniciada com nenhum caractere. 

Eu irei contabilizar seus chutes e se você acertou ou não. 

Caso erre, você precisará tentar uma nova letra ainda não usada. 

Irei representar os caracteres ainda não encontrados como sendo '_' separados por espaços.

Por exemplo '_ _ _ _ _' representa uma palavra de 5 caracteres que ainda não foram descobertos.

'ca _ _ _' representa uma palavra de 5 caracteres cujos 2 primeiros são conhecidos ('ca') e os demais ainda precisam ser descobertos.

O jogo acaba quando você descobrir cada um dos caracteres.

É importante que a cada resposta a única coisa que você me retorne seja o caractere que você escolheu para completar cada caractere faltante da palavra.



A frase que você deve adivinhar tem 4 caracteres.



_ _ _ _



Qual seu primeiro chute?
"""