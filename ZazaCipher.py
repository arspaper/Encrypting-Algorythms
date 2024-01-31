from CaesarCipher import encryptCS, decryptCS


def encryptZA(txt, pattern, mydata):
    letterlower = 'abcdefghijklmnopqrstuvwxyz'
    letterupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pattern = pattern.split()
    out_txt = ""
    shift = 0
    for chrc in txt:
        if chrc in letterlower:
            chrc = chrc.upper()
        elif chrc in letterupper:
            chrc = chrc.lower()
        out_txt += encryptCS(chrc, len(pattern[shift]), mydata)
        shift += 1
    return out_txt


def decryptZA(txt, pattern, mydata):
    letterlower = 'abcdefghijklmnopqrstuvwxyz'
    letterupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pattern = pattern.split()
    out_txt = ""
    shift = 0
    for chrc in txt:
        if chrc in letterlower:
            chrc = chrc.upper()
        elif chrc in letterupper:
            chrc = chrc.lower()
        out_txt += decryptCS(chrc, len(pattern[shift]), mydata)
        shift += 1
    return out_txt
