from gpt import API
from game import *
from entropy import *
from prompts import *
import re
import pandas as pd
import time

lista_de_palavras = []

with open("frases.txt", "r") as f:
    for line in f:
        lista_de_palavras.append(line[:-1])


dict_word_to_guess = []

for sentence in lista_de_palavras[20:41]:
    api = API()

    content = [
        {"role": "system", "content": MAINS_INSTRUCTIONS},
        {"role": "user", "content": first_chute(len(lista_de_palavras[0]))},
    ]
    print(first_chute(len(lista_de_palavras[0])))
    api.send_message(content)
    
    progress_string = ""
    try_num = []
    print("FRASE:",sentence)
    for i, s in enumerate(sentence):
        
        guess_num = 0
        is_guess_correct = False
        guesses = []  # letters guessed
        current_available_chars = available_chars.copy()
        trys = 0
        interromper = False
        while not is_guess_correct:
            
            response = api.get_response()
            response = response.lower()
            print(response)
            if len(response) > 2:
                # match = re.search(r"(?:escolher|chutar)\s+essa?\s+letra\s+[\'\"]([a-z ])[\'\"]", response)
                # match2 = re.search(r"\s+[\'\"]([a-z ])[\'\"]", response)

                # if match:
                #     guess = match.group(1)
                #     print("Letra:", guess)
                # if match2:
                #     guess = match2.group(1)
                #     print("Letra:", guess)
                # else:
                #     guess = response[0]
                #     print("Letra:", guess)
                guess = response.split("\"")[1]
                print("Letra:", guess)
            else:
                guess = response[0]
                print("Letra:", guess)
            
            guess = guess.lower()
            extra_aux = ""
            if guess == "ç":
                guess = " "
            
            if trys > 5:
                guess = current_available_chars[0]

            guess_invalid = guess
            
            if guess == "ã" or guess == "á" or guess == "à" or guess == "â" or guess == "ä" or guess == "ã":
                extra_aux = f"{guess} NÃO É UM CARACTERE VÁLIDO. REPITO, NÃO É UM CARACTERE VÁLIDO. TENTE NOVAMENTE COM UM CARACTERE VÁLIDO.\n"
                guess_invalid = guess
                guess = "a"

            if guess == "é" or guess == "ê" or guess == "è" or guess == "ë" or guess == "ẽ" or guess == "ê":
                extra_aux = f"{guess} NÃO É UM CARACTERE VÁLIDO. REPITO, NÃO É UM CARACTERE VÁLIDO. TENTE NOVAMENTE COM UM CARACTERE VÁLIDO.\n"
                guess_invalid = guess
                guess = "e"
            
            if guess == "í" or guess == "î" or guess == "ì" or guess == "ï" or guess == "ĩ" or guess == "î":
                extra_aux = f"{guess} NÃO É UM CARACTERE VÁLIDO. REPITO, NÃO É UM CARACTERE VÁLIDO. TENTE NOVAMENTE COM UM CARACTERE VÁLIDO.\n"
                guess_invalid = guess
                guess = "i"

            if guess == "ó" or guess == "ô" or guess == "ò" or guess == "õ" or guess == "ö" or guess == "ô":
                extra_aux = f"{guess} NÃO É UM CARACTERE VÁLIDO. REPITO, NÃO É UM CARACTERE VÁLIDO. TENTE NOVAMENTE COM UM CARACTERE VÁLIDO.\n"
                guess_invalid = guess
                guess = "o"

            if guess == "ú" or guess == "û" or guess == "ù" or guess == "ü" or guess == "ũ" or guess == "û":
                extra_aux = f"{guess} NÃO É UM CARACTERE VÁLIDO. REPITO, NÃO É UM CARACTERE VÁLIDO. TENTE NOVAMENTE COM UM CARACTERE VÁLIDO.\n"
                guess_invalid = guess
                guess = "u"
            
            if len(current_available_chars) == 1:
                guess = current_available_chars[0]
                extra_aux = f"Você não tem mais opções de caracteres para escolher. O caractere {guess} é o único disponível.\n"

            is_a_valid_guess = check_is_valid_guess(guess)

            if not is_a_valid_guess:
                aux_prompt = extra_aux + "Por favor, um caractere por vez.\n"
            else:
                aux_prompt = (
                    f"Frase atual: \"{progress_string}\"\n"
                )
                aux_prompt += extra_aux
                is_guess_correct = check_guess(guess=guess, correct=s)

                if is_guess_correct:
                    try_num.append(guess_num + 1)
                    progress_string += s
                    current_available_chars = available_chars.copy()
                    aux_prompt += "Parabéns, você acertou! \n"
                    aux_prompt += "Frase a atual: "
                    aux_prompt += f"\"{progress_string}\""
                    aux_prompt += f"\nBoa tentativa! você escolheu correto com {guess_num + 1} tentativas."
                else:
                    aux_prompt += f"Você errou! \n"
                    aux_prompt += f"Tente novamente, por favor! Você tentou {guess_num} vezes até agora.\n"
                    aux_prompt += (
                        "Caracteres usados até agora: " + ", ".join(guesses) + "\n"
                    )
                    if guess not in guesses:
                        if guess in current_available_chars:
                            guess_num += 1
                            guesses.append(guess)
                            current_available_chars.remove(guess)
                        else:
                            aux_prompt += f"Esse caractere {guess} não faz parte dos caracteres disponíveis. Tente outro caractere, por favor!\n"
                    else:
                        aux_prompt += f'Você já tentou esse caracter "{guess_invalid}", o próximo caractere não é "{guess_invalid}". Tente outro caractere, por favor!\n\n'
                        aux_prompt += f'O próximo caractere NÃO é "{guess_invalid}". VOCÊ NÃO DEVE TENTAR "{guess_invalid}" NOVAMENTE. Tente outro caractere que esteja disponível!\n'
                        aux_prompt += f'O próximo caractere NÃO é "{guess_invalid}". VOCÊ NÃO DEVE TENTAR "{guess_invalid}" NOVAMENTE. Tente outro caractere que esteja disponível!\n'
                        aux_prompt += f'O próximo caractere NÃO é "{guess_invalid}". VOCÊ NÃO DEVE TENTAR "{guess_invalid}" NOVAMENTE. Tente outro caractere que esteja disponível!\n\n'
                        aux_prompt += (
                            f"Não reponda nenhum dos seguintes caracteres {guesses}\n\n"
                        )
                        aux_prompt += "Caracteres disponíveis: " + ", ".join(
                            current_available_chars
                        )
                        trys += 1
                        if trys > 5:
                            aux_prompt += "\nVocê já tentou muitas vezes, por favor, tente outro caractere.\n"

            aux_prompt += "\nPor favor, me diga o próximo caractere seguindo o modelo 'Eu vou escolher o caractere \"_\"':\n\nLembrando que"
            aux_prompt += "Você só pode sugerir um caractere por resposta (apenas letras ou espaço).\n"
            aux_prompt += "Lembre da exceção quando você for escolher o caracter \" \", nesse caso você deve responder: 'Eu vou escolher o caractere \"ç\"'\n"
            aux_prompt += f"A lista de caracteres disponíveis é a seguinte {current_available_chars}"
            aux_prompt += "\nVOCÊ SÓ PODE ESCOLHER CARACTERES QUE ESTEJAM DISPONÍVEL E NÃO DEVE ESCOLHER CARACTERES COM ACENTOS OU CEDILHAS.\n\n"
            print(aux_prompt)
            # time.sleep(0.1)
            content = [{"role": "user", "content": aux_prompt}]
            api.send_message(content)

            time.sleep(0.1)

            if trys > 100:
                interromper = True
                break
        if interromper:
            break

    if not interromper:
        dict_word_to_guess.append((sentence, try_num))
        with open("resultados_novo.txt", "a") as f:
            f.write(f"{sentence}: {str(try_num)}" + "\n")


# save table
# df = pd.read_csv("results.csv")
# df_aux= pd.DataFrame(columns=["sentence", "tries"], data=dict_word_to_guess)

# # concat
# df = pd.concat([df, df_aux], axis=0)
# df.drop_duplicates(inplace=True)
# df.reset_index(drop=True, inplace=True)
# df.to_csv("results.csv", index=False)

# append results in txt

# df.to_csv("results.csv")
