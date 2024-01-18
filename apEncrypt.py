import random
from CaesarCipher import encryptCS, decryptCS
from main import mydata


def encryptAP(txt, key_sentence, shift, line_size, mydata):
    if line_size < len(key_sentence):
        return "INVALID LINE SIZE"
    if len(txt) > len(key_sentence):
        return "ERROR TARGET LINE MUST BE SHORTER THAN KEY SENTENCE"

    key_list = key_sentence.split()  # list with words from key sentence
    line = ''.join(random.choice(mydata) for i in range(line_size))  # generating line of ascii
    line_list = list(line)
    key_word_length = list()
    crypted_key_list = list()

    for key_word in key_list:  # encrypting keywords from key sentence
        key_word_length.append(len(key_word))
        crypted_key_list.append(encryptCS(key_word, shift, mydata))

    for crypted_key_word in crypted_key_list:  # making sure that there are no subsequences of crypted keywords
        line = line.split(crypted_key_word)
        line = "".join(line)

    txt_parts = list()  # parts of the target word
    for length in key_word_length:
        if length > len(txt):
            txt_parts.append(txt)
            txt = ""
            break
        txt_parts.append(txt[:length])
        txt = txt[length:]

    if txt in "":
        txt_parts.pop(len(txt_parts) - 1)

    encrypted_list = list()
    for i in range(len(txt_parts)):
        a = crypted_key_list[i] + encryptCS(txt_parts[i], len(txt_parts[i]), mydata)
        encrypted_list.append(a)

    for i in range(len(encrypted_list)):
        line_list.insert(random.randint(1, len(line) - 1), "Ж")

    line_list = "".join(line_list).split("Ж")
    out_line = ''

    for i in range(len(encrypted_list)):
        out_line += line_list[i] + encrypted_list[i]

    out_line += line_list[-1]
    print(out_line)
    return out_line


def decryptAP(line, key_sentence, shift, mydata):
    crypted_key_list = list()
    key_list = key_sentence.split()
    out_words = list()
    key_length = list()
    for key_word in key_list:
        crypted_key_list.append(decryptCS(key_word, shift, mydata))
        key_length.append(len(key_word))

    print(crypted_key_list)

    for i in range(len(crypted_key_list)):
        ind = line.find(crypted_key_list[i])
        a = line[ind + key_length:ind + 2 * key_length[i]]
        print(decryptCS(a, key_length[i], mydata))
        out_words.append(decryptCS(a, key_length[i], mydata))

    print(out_words)


z = encryptAP("YO TEST MESSAGE", "ANDREY PTITSYN", 4, 100, mydata)

decryptAP(z, "ANDREY PTITSYN IS THE GOAT", 4, mydata)
