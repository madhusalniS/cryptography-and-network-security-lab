## Problem Statement

Classical substitution and transposition ciphers form the foundational concepts of modern cryptography. However, basic implementation challenges—such as handling non-alphabetic characters, computing matrix modular inverses, and managing odd-length string paddings—often lead to vulnerabilities or incorrect encryptions.

This project implements three fundamental classical ciphers to compare their complexity, security levels, and implementation constraints:

1. **Caesar Cipher:** A monoalphabetic substitution cipher shifting characters by a fixed key $k$.
   $$C \equiv (P + k) \pmod{26}$$

2. **Playfair Cipher:** A polygraphic substitution cipher encoding pairs of letters (digraphs) using a $5 \times 5$ grid of letters based on a key phrase.

3. **Hill Cipher:** A polygraphic substitution cipher using linear algebra. Plaintext blocks are converted into vectors and multiplied by a $n \times n$ key matrix $K$ modulo 26:
   $$C \equiv K \cdot P \pmod{26}$$

### Objectives & Deliverables
- [ ] Implement encryption and decryption routines for Caesar, Playfair, and Hill ciphers.
- [ ] Ensure proper matrix invertibility checks for the Hill cipher ($\gcd(\det(K), 26) = 1$).
- [ ] Implement digraph formatting and null-character padding (e.g., inserting 'X') for the Playfair cipher.
- [ ] Include automated test suites verifying known test vectors for each cipher.
