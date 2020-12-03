def get_subset(str_set, index):
    if len(str_set) == index:
        new_set = []
        subsets = []
        subsets.append(new_set)
        return subsets
    else:
        subsets = get_subset(str_set, index+1)
        new_item = str_set[index]
        new_subset = []
        for s in subsets:
            new_set = s.copy()
            new_set.append(new_item)
            new_subset.append(new_set)
        subsets.extend(new_subset)
        return subsets

print(get_subset(["a", "b", "c"], 0))
