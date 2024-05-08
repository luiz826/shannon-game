import numpy as np


def calc_upper_bound(guesses):

    context_len = len(guesses)
    alfabeth_len = 27
    
    count_probs = {k: 0 for k in range(1, alfabeth_len + 1)}

    for g in guesses:
        count_probs[g] += 1

    upper_entropy = 0

    for k, v in count_probs.items():
        if v == 0:
            continue
        p = v / context_len
        upper_entropy += (p) * np.log2(1/p) 

    return upper_entropy 


def calc_lower_bound(guesses):
    context_len = len(guesses)
    alfabeth_len = 27
    
    count_probs = {k: 0 for k in range(1, alfabeth_len + 1)}

    for g in guesses:
        count_probs[g] += 1

    lower_entropy = 0

    for n in range(1, alfabeth_len):

        p_1 = count_probs[n] / context_len
        p_2 = count_probs[n + 1] / context_len
        lower_entropy += n * (p_1 - p_2) * np.log2(n)

    return lower_entropy


if "__main__" == __name__:
    # Testando as funções com o feedback do professor
    guesses = [2, 1, 1, 1, 11, 3, 2, 5, 1, 1, 1, 15]

    print(calc_upper_bound(guesses))
    print(calc_lower_bound(guesses))


