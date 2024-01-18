def encryptCS(txt, shift, mydata):
    out_txt = ""
    for i in range(len(txt)):
        if txt[i] not in mydata:
            return "NOT ASCII TXT"
        tgt_index = mydata.find(txt[i])
        if abs(shift + tgt_index) >= len(mydata):
            out_txt += mydata[(shift + tgt_index) % len(mydata)]
        else:
            out_txt += mydata[shift + tgt_index]
    return out_txt


def decryptCS(txt, shift, mydata):
    out_txt = ""
    shift = -1 * shift
    for i in range(len(txt)):
        if txt[i] not in mydata:
            return "NOT ASCII TXT"
        tgt_index = mydata.find(txt[i])
        if abs(shift + i) >= len(mydata):
            out_txt += mydata[(shift + tgt_index) % len(mydata)]
        else:
            out_txt += mydata[shift + tgt_index]
    return out_txt
