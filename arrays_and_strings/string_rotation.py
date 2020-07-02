def str_rotation(str1, str2):
    if len(str1) == len(str2):
        new_str = str2 + str2
        if str1 in new_str:
            return True
        else:
            return False


if __name__ == "__main__":
    out = str_rotation("waterbottle", "erbottlewat")
    if out:
        print("Is rotated")
    else:
        print("Not rotated")
