mydata = "#$%+()'*&,-./0123456789:;<=>?\@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def encryptVE(txt):
    out_txt = ""
    global mydata, shift
    for i in range(len(txt)):
        if txt[i] not in mydata:
            return "NOT ASCII TXT"
        tgt_index = mydata.find(txt[i])
        if abs(shift + tgt_index) > len(mydata):
            out_txt += mydata[(shift + tgt_index) % len(mydata)]
        else:
            out_txt += mydata[shift + tgt_index]
    return out_txt


def decryptVE(txt):
    out_txt = ""
    global mydata, shift
    shift = -1 * shift
    for i in range(len(txt)):
        if txt[i] not in mydata:
            return "NOT ASCII TXT"
        tgt_index = mydata.find(txt[i])
        if abs(shift + i) > len(mydata):
            out_txt += mydata[(shift + tgt_index) % len(mydata)]
        else:
            out_txt += mydata[shift + tgt_index]
    return out_txt


shift = int(input("Введите сдвиг: "))
