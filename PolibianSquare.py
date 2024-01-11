def encryptPS(txt, table):
    out_list = list()
    for chrc in txt:
        chrc = chrc.lower()
        if not chrc.isascii():
            return "NOT ASCII"
        for i in range(len(table)):
            if chrc in table[i]:
                out_list.append(f"{str(i + 1)}{str(''.join(table[i]).find(chrc) + 1)}")
                break
    return out_list


def decryptPS(my_str, table):
    out_txt = ""
    my_list = my_str.split()
    for indexes in my_list:
        if len(indexes) != 2:
            return "INVALID INDEXES"
        i, j = int(indexes[0]) - 1, int(indexes[1]) - 1
        if (0 <= i <= 6) and (0 <= j <= 6):
            out_txt += table[i][j]
        else:
            return "INVALID INDEXES"
    return out_txt
