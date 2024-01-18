from CaesarCipher import encryptCS, decryptCS


def encryptVE(txt, pattern, mydata):
    out_txt = ""
    shift = 0
    for chrc in txt:
        if shift == len(pattern):
            shift = 0
        out_txt += encryptCS(chrc, pattern[shift], mydata)
        shift += 1
    return out_txt


def decryptVE(txt, pattern, mydata):
    out_txt = ""
    shift = 0
    for chrc in txt:
        if shift == len(pattern):
            shift = 0
        out_txt += decryptCS(chrc, pattern[shift], mydata)
        shift += 1
    return out_txt
