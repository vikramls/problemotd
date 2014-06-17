import string
from itertools import cycle, product

"""Problem from http://www.problemotd.com/problem/vigenere-cipher/"""

alphabet = string.ascii_uppercase

def encrypt(msg, key):
    keyseq = cycle(key)
    ciphertext = []
    for c in msg.upper():
        _s = ord(c) + ord(keyseq.next()) - 2*ord('A')
        q, r = divmod(_s, 26)
        ciphertext.append(alphabet[r])

    return ''.join(ciphertext)

def decrypt(cipher, key):
    keyseq = cycle(key)
    plaintext = []
    for c in cipher.upper():
        _s = ord(c) - ord(keyseq.next()) - 2*ord('A')
        q, r = divmod(_s, 26)
        plaintext.append(alphabet[r])
        
    return ''.join(plaintext)

def bruteforce(cipher):
    _a = ' ' + alphabet
    keygen = product(_a, _a, _a, _a, _a)
    keys_seen = {}
    for _key in keygen:
        if _key in keys_seen:
            continue
        key = ''.join(_key).strip()
        if not key:
            continue
        plaintext = decrypt(cipher, key)
        # This is a hack, need to figure out how to detect plaintext.
        if 'WELCOME' in plaintext:
            print plaintext, key
            break
        keys_seen.setdefault(key, 0)

print encrypt('TODAYISMYBIRTHDAY', 'REDDIT')
print decrypt(encrypt('TODAYISMYBIRTHDAY', 'REDDIT'), 'REDDIT')
bruteforce('ZEJFOKHTMSRMELCPODWHCGAW')
