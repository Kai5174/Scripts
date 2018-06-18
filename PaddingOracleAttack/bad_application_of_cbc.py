from CBC_cipher import CBCCipher
import base64
from Crypto import Random
import binascii

"""
Demonstrate the way padding oracle attack
"""


SECRET_KEY = 'Damnsecretkey'
target_msg = input('input a message:')


class server():
    server_cipher = None

    def __init__(self, key):
        self.server_cipher = CBCCipher(key)

    def encrypt(self, msg):
        return self.server_cipher.encrypt(msg)

    def decrypt(self, ciphertext):
        return self.server_cipher.is_padding_correct(ciphertext)

"""
Server generate the cipher text
"""

# Server encrypt the target message
server = server(SECRET_KEY)
target_cipher_text = server.encrypt(target_msg)


"""
Attacker obtain the cipher text,
and perform oracle attack
"""

# Attacker obtain the encrypted_msg, try to reveal the plaintext
# and controlled the server's decrypt

BLOCK_SIZE = 16

target = base64.b64decode(target_cipher_text)

iv = bytearray(target[:BLOCK_SIZE])
c2 = bytearray(target[BLOCK_SIZE:])

numBlocks = int(len(c2)/BLOCK_SIZE)
I = bytearray(b'\x00'*len(c2))
P = bytearray(b'\x00'*len(c2))

for ii in range(numBlocks):
    cur_block = c2[ii*BLOCK_SIZE:(ii+1)*BLOCK_SIZE]
    c1 = bytearray(b'?'*BLOCK_SIZE)
    counter = 0
    for startPad in reversed(range(BLOCK_SIZE)):
        numPad = BLOCK_SIZE - startPad
        for tmp in range(1, numPad+1):
            c1[-tmp] = numPad ^ I[(ii+1)*BLOCK_SIZE-tmp]
        counter = 0
        c1[-numPad] = counter
        msg = iv+c1+cur_block
        while not server.decrypt(base64.b64encode(bytes(msg))):
            counter += 1
            c1[-numPad] = counter
            msg = iv+c1+cur_block
        I[ii*BLOCK_SIZE+startPad] = counter ^ numPad
        P[ii*BLOCK_SIZE+startPad] = I[ii*BLOCK_SIZE+startPad]^c2[ii*BLOCK_SIZE+startPad]

result = bytearray()
for kk in range(numBlocks):
    cc = target[kk*BLOCK_SIZE:(kk+1)*BLOCK_SIZE]
    for ii in range(BLOCK_SIZE):
        result.append(cc[ii]^I[kk*BLOCK_SIZE+ii])

print('The cracked data:')
print(result)
