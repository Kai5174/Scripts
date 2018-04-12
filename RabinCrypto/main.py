"""
In the purpose of understanding the robin crypto.

Resource: example of wiki: https://en.wikipedia.org/wiki/Rabin_cryptosystem
Usage: python main.py [message in integer]
"""
import sys


def CRT(r1, p1, r2, p2):
    """
    Perform chinese reminder calculation, defined as following, this function only work when p1, p2 are prime number
        x % p1 = r1
        x % p2 = r2
    return x
    """
    M = p1 * p2
    M1 = p2
    M2 = p1

    # if p1, p2 are prime number
    N1 = pow(M1, p1-2, p1)
    N2 = pow(M2, p2-2, p2)

    return (r1*M1*N1 + r2*M2*N2) % M


def sqrt_modulo(c, p):
    c = c % p
    # p must be prime
    a1 = pow(c, round((p+1)/4), p)
    a2 = -a1 % p
    return a1, a2


if __name__ == '__main__':
    # Bob's public key and private key
    bob_priv = (7, 11)
    bob_pub = bob_priv[0] * bob_priv[1]

    # Alice prepared message
    m = int(sys.argv[1])
    print("origin message is {}".format(m))
    c = pow(m, 2, bob_pub)
    print("cipher text is {}".format(c))

    # Bob decrypt the message
    m_p1, m_p2 = sqrt_modulo(c, bob_priv[0])
    m_q1, m_q2 = sqrt_modulo(c, bob_priv[1])

    print(m_p1)
    print(m_p2)
    print(m_q1)
    print(m_q2)

    # play chinese reminder
    m1 = CRT(m_p1, bob_priv[0], m_q1, bob_priv[1])
    m2 = CRT(m_p1, bob_priv[0], m_q2, bob_priv[1])
    m3 = CRT(m_p2, bob_priv[0], m_q2, bob_priv[1])
    m4 = CRT(m_p2, bob_priv[0], m_q1, bob_priv[1])

    print("possible answer are:")
    print("m1 = {}".format(m1))
    print("m2 = {}".format(m2))
    print("m3 = {}".format(m3))
    print("m4 = {}".format(m4))

