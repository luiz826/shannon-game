from game import available_chars

MAINS_INSTRUCTIONS = """
Você vai jogar o jogo de shannon. 
Você precisa descobrir todos os caracteres de uma frase cujo alfabeto são as 26 letras do alfabeto minúsculas mais o caractere de espaço, logo, 27 caracteres ao todo.
Você só pode sugerir um caractere por resposta.
Você não pode repetir chutes já feitos.
Uma vez que você acertou um caractere, deve prever o próximo caractere com base no conhecimento dos caracteres anteriores. Além disso, você pode sugerir caracteres chutados em tentativas anteriores, pois a cada acerto, a lista de caracteres já chutados por você é reiniciada com nenhum caractere. 
Eu irei contabilizar seus chutes e se você acertou ou não. 
Caso erre, você precisará tentar um novo caractere ainda não usado. 
Irei representar os caracteres ainda não encontrados como sendo '_' concatenados.
Por exemplo '___' representa uma palavra de 5 caracteres que ainda não foram descobertos.
'ca___' representa uma palavra de 5 caracteres cujos 2 primeiros são conhecidos ("ca") e os demais ainda precisam ser descobertos.
O jogo acaba quando você descobrir cada um dos caracteres.
É importante que a cada resposta a única coisa que você me retorne seja o caractere que você escolheu para completar cada caractere faltante da palavra.
Reforçando: quero que sua resposta seja apenas o caractere que você escolheu para o caracter faltante atual da palavra.
Muito importante! Você deve jogar o jogo até o final, ou seja, até descobrir todos os caracteres da palavra.
Você não pode desistir no meio do jogo. Você não pode responder outra coisa que não seja o caractere que você escolheu para completar o caractere faltante atual da palavra.
Lembrando novamente: Você precisa descobrir todos os caracteres de uma frase cujo alfabeto são as 26 letras do alfabeto minúsculas mais o caractere de espaço, logo, 27 caracteres ao todo.
Não me peça para adivinhar a palavra, você deve que descobrir ela, caractere por caractere.

Exemplo de resposta que você sempre deve dar. Repito, você sempre precisa responder nesse modelo:

'Eu vou escolher o caractere "_"'. No qual esse _ representa um dos 27 caracteres possíveis.

Existirá uma exceção quando você for escolher o caracter espaço, nesse caso você deve responder: 'Eu vou escolher o caractere "ç"'.
"""


def first_chute(n):
    aux = f"A frase que você deve adivinhar tem {n} caracteres.\n"
    aux += f"A lista de caracteres disponíveis é a seguinte {available_chars}"
    return aux + "Por favor, me diga o próximo caractere seguindo o modelo 'Eu vou escolher o caractere \"_\"':\n"
