def result(guess, soln):
    guess_dict = {}
    for i in range(len(guess)):
        item = guess[i]
        if item in guess_dict:
            guess_dict[item].append(i)
        else:
            guess_dict[item] = [i]

    soln_dict = {}
    for i in range(len(soln)):
        item = soln[i]
        if item in soln_dict:
            soln_dict[item].append(i)
        else:
            soln_dict[item] = [i]

    hits = 0
    pseudo_hits = 0
    for item in soln_dict:
        soln_index = soln_dict[item]
        guess_index = guess_dict.get(item, None)
        if guess_index:
            match_index = set(soln_index).intersection(set(guess_index))
            if match_index:
                hits += len(match_index)
                if len(match_index) < len(guess_index):
                    pseudo_hits += len(guess_index) - len(match_index)
            else:
                pseudo_hits += len(guess_index)

    print(hits)
    print(pseudo_hits)


result("RGGB", "RGGB")
