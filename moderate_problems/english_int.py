smalls = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
          "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

bigs = ["", "Thousand", "Million", "Billion"]
hundred = "Hundred"
negative = "Negative"


def convert_to_english(num):
    if num == 0:
        return smalls[0]
    elif num < 0:
        return negative + " " + convert_to_english(-1 * num)

    chunk_count = 0
    num_data = []
    while num > 0:
        if num % 1000 != 0:
            chunk = convert_chunk(num % 1000) + " " + bigs[chunk_count]
            num_data.insert(0, chunk)
        num //= 1000
        chunk_count += 1
    print(' '.join(num_data))
    return ' '.join(num_data)


def convert_chunk(num):
    num_data = []
    if num >= 100:
        num_data.append(smalls[num//100])
        num_data.append(hundred)
        num %= 100

    if 19 >= num >= 10:
        num_data.append(smalls[num])
    elif num >= 20:
        num_data.append(tens[num//10])
    num %= 10

    if 9 >= num >= 1:
        num_data.append(smalls[num])
    return ''.join(num_data)


if __name__ == "__main__":
    convert_to_english(-1234)
