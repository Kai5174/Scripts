"""
This script is just for learning purpose. Involves


If target sends the same message to different parties,
Party1's public key (n1, e), private key d1.
Party2's public key (n2, e), private key d2.

Alice sends message m to these three parties


"""
import sys


def get_priv_key(p, q, e):
    k = 1
    while ((p-1)*(q-1)*k+1) % e != 0:
        k += 1
    return int(((p-1)*(q-1)*k+1)/e)


def retrieve_modulo(c, e, M):
    k = 0
    while (round((c+k*M)**(1/e))**e-(c+k*M)!= 0):
        k += 1
    return round((c+k*M)**(1/e))

# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

##

if __name__ == '__main__':

    # Parties info
    p1_pub = (87, 3)    # 87 = 3*29
    p1_pri = get_priv_key(3, 29, p1_pub[1])

    p2_pub = (115, 3)   # 115 = 5*23
    p2_pri = get_priv_key(5, 23, p2_pub[1])

    # Alice do encryption
    m = int(sys.argv[1])
    print("Alice send the message {}".format(m))

    c1 = pow(m, p1_pub[1], p1_pub[0])
    print("ciphertext 1 is {}".format(c1))

    c2 = pow(m, p2_pub[1], p2_pub[0])
    print("ciphertext 2 is {}".format(c2))


    # Parties retrieve plain text
    m1 = pow(c1, p1_pri, p1_pub[0])
    print("party 1 got the message {}".format(m1))

    m2 = pow(c2, p2_pri, p2_pub[0])
    print("party 2 got the message {}".format(m2))


    # Eve cracking the encryption
    """
    Eve only know the c1, c2, c3, and p1_pub, p2_pub, p3_pub
    """

    M  = p1_pub[0]*p2_pub[0]
    M1 = p2_pub[0]
    M2 = p1_pub[0]

    N1 = modinv(M1, p1_pub[0])
    N2 = modinv(M2, p2_pub[0])

    x = (c1*M1*N1 + c2*M2*N2) % M
    print("Eve get the message by CRT: {}".format(retrieve_modulo(x, p1_pub[1], M)))


