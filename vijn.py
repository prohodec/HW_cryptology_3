from itertools import cycle

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode_vijn(text, keytext):
    text = text.upper()
    keytext = keytext.upper()
    for char in text:
        if char not in alp:
            text = text.replace(char, '')
    for char in keytext:
        if char not in alp:
            keytext = keytext.replace(char, '')

    f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 26) % 26]
    return ''.join(map(f, zip(text, cycle(keytext))))


def decode_vijn(coded_text, keytext):
    text = coded_text.upper()
    keytext = keytext.upper()
    for char in text:
        if char not in alp:
            text = text.replace(char, '')
    for char in keytext:
        if char not in alp:
            keytext = keytext.replace(char, '')

    f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % 26]
    return ''.join(map(f, zip(coded_text, cycle(keytext))))


if __name__ == '__main__':
    while True:
        word = input("Enter a word(0 to exit): ")
        if word == "0":
            break
        key = input("Enter a key: ")
        enc_word = encode_vijn(word, key)
        print("encrypted word:", enc_word)
        print("decrypted word:", decode_vijn(enc_word, key))
