def convert_bin_to_octal(num_bin):
    BIT = 3
    num_oct = []
    octal = []

    while num_bin:
        cnt, sum_ = 0, 0
        while cnt < BIT and num_bin:
            octal.append(int((num_bin.pop())))
            cnt += 1

        sum_ = convert_octal(octal)
        num_oct.append(sum_)

    num_oct = "".join(map(str, num_oct[::-1]))