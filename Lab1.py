import numpy as np
from math import gcd

# Caesar
def caesar(text, key, decrypt=False):
    if decrypt:
        key = -key
    return ''.join(
        chr((ord(c.upper()) - 65 + key) % 26 + 65) if c.isalpha() else c
        for c in text
    )


# Playfair
class Playfair:
    def __init__(self, key):
        key = ''.join(dict.fromkeys(
            key.upper().replace('J', 'I') +
            'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        ))
        self.m = [key[i:i+5] for i in range(0, 25, 5)]

    def pos(self, c):
        for r in range(5):
            for col in range(5):
                if self.m[r][col] == c:
                    return r, col

    def prepare(self, text):
        text = ''.join(c for c in text.upper() if c.isalpha()).replace('J', 'I')
        out, i = '', 0
        while i < len(text):
            a = text[i]
            if i + 1 == len(text):
                out += a + 'X'
                i += 1
            elif text[i + 1] == a:
                out += a + 'X'
                i += 1
            else:
                out += a + text[i + 1]
                i += 2
        return out

    def encrypt(self, text):
        text = self.prepare(text)
        return self.process(text, 1)

    def decrypt(self, text):
        return self.process(text, -1)

    def process(self, text, s):
        ans = ''
        for i in range(0, len(text), 2):
            a, b = text[i:i+2]
            r1, c1 = self.pos(a)
            r2, c2 = self.pos(b)

            if r1 == r2:
                ans += self.m[r1][(c1+s) % 5] + self.m[r2][(c2+s) % 5]
            elif c1 == c2:
                ans += self.m[(r1+s) % 5][c1] + self.m[(r2+s) % 5][c2]
            else:
                ans += self.m[r1][c2] + self.m[r2][c1]
        return ans


# Hill
class Hill:
    def __init__(self, key):
        self.k = np.array(key)
        det = int(round(np.linalg.det(self.k))) % 26
        if gcd(det, 26) != 1:
            raise ValueError("Invalid key matrix")

        invdet = pow(det, -1, 26)
        a, b = self.k[0]
        c, d = self.k[1]
        self.inv = invdet * np.array([[d, -b], [-c, a]]) % 26

    def encrypt(self, text):
        text = ''.join(c for c in text.upper() if c.isalpha())
        text += 'X' * (len(text) % 2)
        return self.process(text, self.k)

    def decrypt(self, text):
        return self.process(text, self.inv)

    def process(self, text, key):
        ans = ''
        for i in range(0, len(text), 2):
            v = np.array([[ord(text[i])-65], [ord(text[i+1])-65]])
            r = key.dot(v) % 26
            ans += ''.join(chr(int(x)+65) for x in r.flatten())
        return ans


# Menu
while True:
    print("\n1. Caesar  2. Playfair  3. Hill  4. Exit")
    ch = input("Choice: ")

    if ch == '1':
        text = input("Text: ")
        key = int(input("Key: "))
        e = caesar(text, key)
        print("Encrypted:", e)
        print("Decrypted:", caesar(e, key, True))

    elif ch == '2':
        key = input("Key: ")
        text = input("Text: ")
        p = Playfair(key)
        e = p.encrypt(text)
        print("Encrypted:", e)
        print("Decrypted:", p.decrypt(e))

    elif ch == '3':
        key = [
            list(map(int, input("Row 1: ").split())),
            list(map(int, input("Row 2: ").split()))
        ]
        text = input("Text: ")
        try:
            h = Hill(key)
            e = h.encrypt(text)
            print("Encrypted:", e)
            print("Decrypted:", h.decrypt(e))
        except ValueError as err:
            print(err)

    elif ch == '4':
        break

    else:
        print("Invalid choice")
