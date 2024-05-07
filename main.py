from gpt import API
from game import *
from entropy import *
from prompts import *
import re 
import pandas as pd

lista_de_palavras = ["arma"]
api = API()
dict_word_to_guess = {}
for i in range(1):
    sentence = lista_de_palavras[i]
    
    content = [
        {"role": "system","content": MAINS_INSTRUCTIONS},
        {"role": "user","content": first_chute(len(lista_de_palavras[0]))},
    ]
    print(first_chute(len(lista_de_palavras[0])))
    api.send_message(content)
    
    progress_string = ["_"] * len(sentence)
    try_num = []

    for i, s in enumerate(sentence):
        guess_num = 0
        is_guess_correct = False
        guesses = [] # letters guessed

        while not is_guess_correct:
            response = api.get_response()
            if len(response) > 2:
                match = re.search(r"letra\s+[\'\"](\w)[\'\"]", response)
                if match:
                    guess = match.group(1)
                    print("Letra:", guess)
                else:
                    guess = response[0]
                    print("Letra:", guess)
            else:
                guess = response[0]
                print("Letra:", guess)
            guess = guess.lower()
            is_a_valid_guess = check_is_valid_guess(guess)

            if not is_a_valid_guess:
                aux_prompt = "Por favor, uma letra por vez.\n"
            else:
                aux_prompt = "Frase a ser adivinhada: " + "".join(progress_string) + "\n"    
                is_guess_correct = check_guess(guess=guess, correct=s)

                if is_guess_correct:
                    try_num.append(guess_num + 1)
                    progress_string[i] = s
                    aux_prompt += "Parabéns, você acertou! \n"
                    aux_prompt += "Frase a ser adivinhada: "
                    aux_prompt += "" .join(progress_string)
                    aux_prompt += f"\nBoa tentativa! você escolheu correto com {guess_num + 1} tentativas."
                else:
                    aux_prompt += f"Você errou! \n"
                    aux_prompt += f"Tente novamente, por favor! Você tentou {guess_num} vezes até agora.\n"
                    aux_prompt += "Caracteres usados até agora: " + ", ".join(guesses) + "\n"
                    if guess not in guesses:
                        guess_num += 1
                        guesses.append(guess)    
                    else:
                        aux_prompt += f"Você já tentou esse caracter \"{guess}\", o próximo caractere não é \"{guess}\". Tente outro caractere, por favor!\n"

            aux_prompt += "\nPor favor, me diga o próximo caractere:\n\nLembrando que"
            aux_prompt += " você só pode sugerir um caractere por resposta (apenas letras ou espaços).\n"
            
            print(response)
            print(aux_prompt)
            
            # Se ainda não acabou
            if progress_string[-1] != "_":
                content = [{"role": "user", "content": aux_prompt}]
                api.send_message(content)
            
    
    dict_word_to_guess[sentence] = try_num

# save table
df = pd.DataFrame(dict_word_to_guess)
df.to_csv("results.csv")