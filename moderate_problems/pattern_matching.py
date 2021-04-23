def match_pattern(pattern, value):
    size = len(value)
    main_char = pattern[0]
    alt_char = 'b' if main_char == 'a' else 'a'
    main_char_count = count_of(pattern, main_char)
    alt_char_count = len(pattern) - main_char_count
    max_size_main = size//main_char_count
    first_alt = pattern.find(alt_char)

    for i in range(0, max_size_main):
        remaining_length = size - i * main_char_count
        first = value[0:i]
        if alt_char_count == 0 or remaining_length % alt_char_count == 0:
            alt_index = first_alt * i
            alt_size = 0 if alt_char_count == 0 else remaining_length//alt_char_count
            second = value[alt_index: alt_size + alt_index]

            cand = get_string_from_pattern(pattern, first, second)
            if cand == value:
                return True


def get_string_from_pattern(pattern, first, second):
    final_str = ''
    for pat in pattern:
        if pat == 'a':
            final_str += first
        else:
            final_str += second
    return final_str


def count_of(pattern, main_chr):
    count = 0
    for pat in pattern:
        if pat == main_chr:
            count += 1
    return count


if match_pattern("aabab", "catcatgocatgo"):
    print("found")
else:
    print("not found")
