def compress_str(input_str):
    output_str = list()
    chr_count = 0
    for i in range(len(input_str)):
        if i+1 >= len(input_str) or input_str[i] != input_str[i+1]:
            output_str.append(input_str[i])
            output_str.append(str(chr_count))
            chr_count = 0
        chr_count += 1

    return ''.join(output_str)


if __name__ == "__main__":
    inp_str = "aabbc"
    comp_str = compress_str(inp_str)
    if len(inp_str) <= len(comp_str):
        print(inp_str)
    else:
        print(comp_str)
