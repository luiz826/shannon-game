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
