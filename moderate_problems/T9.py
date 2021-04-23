# brute force
t9_dict = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
           7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}


def get_all_str(inp, final_str='', final_str_list=[]):
    if inp is None:
        return final_str
    st = t9_dict[inp.data]
    for item in st:
        final_str += item
        final_str_list.append(get_all_str(inp.next, final_str, final_str_list))

# optimized solution:
# check for words prefix if prefix exist in trie then only move to next step else discard that word
# More optimal solution
# map each word in dictionary to its t9 repr like APPLE-27753 and store in a dict
# get the word from the dict by querying the inp

