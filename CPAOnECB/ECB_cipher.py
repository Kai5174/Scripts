from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64

BLOCK_SIZE = 16  # bytes


class ECBCipher:
    """
    Usage:

    cipher = CBCCipher(key)
    ciphertext = cipher.encrypt(msg)

    """

    key = None          # bytes format
    iv = None           # bytes format
    h = SHA256.new()    # hash function

    def __init__(self, key):

        self.h.update(str.encode(key))

        self.key = str.encode(self.h.hexdigest()[:BLOCK_SIZE])
        self.iv = Random.get_random_bytes(BLOCK_SIZE)
        # self.iv = b'\x01'*BLOCK_SIZE

    def encrypt(self, msg):
        padded_msg = self.pad(msg)
        cipher = AES.new(self.key, AES.MODE_ECB, self.iv)

        return base64.b64encode(self.iv + cipher.encrypt(padded_msg))

    def decrypt(self, ciphertxt):
        ct = base64.b64decode(ciphertxt)
        iv = ct[:BLOCK_SIZE]
        cipher = AES.new(self.key, AES.MODE_ECB, self.iv)
        return self._remove_padding(cipher.decrypt(ct[BLOCK_SIZE:]))

    def is_padding_correct(self, ciphertxt):
        return self.decrypt(ciphertxt) is not None

    @staticmethod
    def pad(msg):
        app_len = BLOCK_SIZE - len(msg) % BLOCK_SIZE
        for ii in range(app_len):
            msg += chr(app_len)
        return msg

    @staticmethod
    def _remove_padding(data):
        # Cited from https://github.com/TheCrowned/padding-oracle-attack/blob/master/oracle.py
        pad_len = data[-1]

        if pad_len < 1 or pad_len > BLOCK_SIZE:
            return None
        for i in range(1, pad_len):
            if data[-i - 1] != pad_len:
                return None
        return data[:-pad_len]

if __name__ == '__main__':
    key = 'securekeythatnooneknows'
    cipher = ECBCipher(key)
    msg = input('Input a plaintext:')

    ciphertext = cipher.encrypt(msg)
    print(len(base64.b64decode(ciphertext)))
    print(len(ciphertext))

    decrptedmsg = cipher.decrypt(ciphertext)
    print(decrptedmsg)
