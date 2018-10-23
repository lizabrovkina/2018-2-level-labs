"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''


if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

def propose_candidates(word: str, max_depths_permutations: int = 1) -> list:
    if word == "" or word is None:
        return []
    if max_depths_permutations == str(max_depths_permutations) or max_depths_permutations is None or int(max_depths_permutations) <= 0:
        return []

    list_1 = []
    for i in range(len(word)):
        new_word = word[:i] + word[(i+1):]
        list_1 += [new_word]

    list_2 = []
    for i in range(len(word)+1):
        for c in LETTERS:
            new_word = word[:i] + c + word[i:]
            list_2 += [new_word]

    list_3 = []
    for i in range(len(word)):
        for c in LETTERS:
            new_word = word[:i] + c + word[(i+1):]
            list_3 += [new_word]

    spl = []
    list_4 = []
    two_rev = []
    left = ""
    right = ""
    for i in word:
        spl += [i]
    for i in range(len(spl)-1):
        two_rev = str(spl[i+1] + spl[i])
        left = "".join(spl[:i])
        right = "".join(spl[i+2:])
        new_word = left + two_rev + right
        list_4 += [new_word]

    without_duplicates = []
    duplicates = list_1 + list_2 + list_3 + list_4
    for b in duplicates:
        if b in without_duplicates:
            continue
        without_duplicates.append(b)
    return without_duplicates

def keep_known(candidates: tuple, frequencies: dict) -> list:
    if candidates is None or type(candidates) is not tuple:
        return []
    if frequencies is None:
        return []

    candidates_list = []
    for k in frequencies.keys():
        if k in candidates:
            candidates_list.append(k)
    return candidates_list


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if candidates is () or candidates is None:
        return 'UNK'
    if frequencies == dict() or frequencies is None:
        return 'UNK'

    freq_k = list(frequencies.keys())
    freq_v = frequencies.values()
    new_v = []
    new_k = []
    for k in freq_k:
        if k not in candidates:
            frequencies.pop(k)
    for v in freq_v:
        new_v.append(v)

    max_v = max(new_v)
    for k,v in frequencies.items():
        if v == max_v:
            new_k.append(k)
    new_k.sort()
    right_word = new_k[0]
    return right_word


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:

    if word is None:
        return 'UNK'
    if frequencies is None:
        return 'UNK'
    if as_is_words:
        if word.upper() in as_is_words:
            return word
    if word in frequencies:
        return word
    every_candidate = propose_candidates(word)
    correct_candidates = tuple(keep_known(tuple(every_candidate), frequencies))
    best_word = choose_best(frequencies, correct_candidates)
    return best_word
