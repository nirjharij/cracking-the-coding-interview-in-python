import sys


def split_str(dictionary, sentence, start):
    if start > len(sentence):
        return 0, ""

    index = start
    best_parsing = None
    best_invalid = sys.maxsize
    partial = ""
    while index < len(sentence):
        c = sentence[index]
        partial += c
        invalid = 0 if partial in dictionary else len(partial)
        if invalid < best_invalid:
            inv, parsed = split_str(dictionary, sentence, index+1)
            if invalid + inv < best_invalid:
                best_invalid = invalid + inv
                best_parsing = partial + " " + parsed
                if best_invalid == 0:
                    break
        index += 1
    return best_invalid, best_parsing
