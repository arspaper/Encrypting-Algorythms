from CaesarCipher import encryptCS, decryptCS
from VigenereCipher import encryptVE, decryptVE
from PolybiusSquare import encryptPS, decryptPS
import random

encryptionTable = [
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['g', 'h', 'i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p', 'q', 'r'],
    ['s', 't', 'u', 'v', 'w', 'x'],
    ['y', 'z', '0', '1', '2', '3'],
    ['4', '5', '6', '7', '8', '9']
]

encryptionCharacters = r"#$%+()'*&,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_ `abcdefghijklmnopqrstuvwxyz{|}~"


l = list(encryptionCharacters)
random.shuffle(l)
mydata = ''.join(l)

