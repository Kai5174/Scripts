from ECB_cipher import ECBCipher
from array_operator import find_repeat, get_block, b64ToBytesArray
import base64
import string

secret_key = "Thedamnsecretkey"


# Suppose this bad server always append something_secret when user add msg
class server():
    server_cipher = None
    something_secret = "HUEWIFBEOIWJIDOIjfewiafjedckahialfewa123291dmdksl,c,!~3298"

    def __init__(self, key):
        self.server_cipher = ECBCipher(key)

    def encrypt(self, msg):
        return self.server_cipher.encrypt(msg+self.something_secret)

vulSever = server(secret_key)


# Suppose CPA attack, attacker can chose any plaintext and get its ciphertext
# Challenge, attacker need to reveal the something_secret
test_msg = 'A'*100
test_ct = vulSever.encrypt(test_msg)
block, blocksize, offset = find_repeat(bytearray(base64.b64decode(test_ct)))

# reveal the first byte
guess_block_number = 5
rec = ''
for bb in range(0, guess_block_number):
    for kk in range(1, blocksize+1):
        ct_tmp = b64ToBytesArray(vulSever.encrypt('A'*(blocksize-kk)))
        # print("The encrypted message {}".format('A'*(blocksize-kk)+rec))
        target_ct = get_block(ct_tmp, blocksize, offset+blocksize*bb)

        STRINGS = string.printable
        for ii in range(len(STRINGS)):
            test_msg = 'A'*(blocksize-kk) + rec + STRINGS[ii]
            # print("The test message {}".format(test_msg))
            test_ct = get_block(b64ToBytesArray(vulSever.encrypt(test_msg)), blocksize, offset+blocksize*bb)
            if target_ct == test_ct:
                rec += '{}'.format(STRINGS[ii])
                break

print(rec)