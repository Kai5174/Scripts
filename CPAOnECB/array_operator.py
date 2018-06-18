import base64
import string
import random

def b64ToBytesArray(b64):
    return bytearray(base64.b64decode(b64))

def get_block(arrayList, block_size, offset):
    return arrayList[offset:offset+block_size]

def find_repeat(arrayList):
    """
    E.g. Suppose we have arraylist = 'asdf012345601234560123456',
    the method would output block = 0123456, length = 7, offset = 4

    :param arrayList:
    :return:
    """

    p0 = 0
    start0 = 0

    p1 = 1
    start1 = 1

    combo = 0

    while True:
        # print(start0, p0, p1, combo, len(arrayList))
        if combo == 0:
            if arrayList[p0] == arrayList[p1]:
                start0 = p0
                start1 = p1
                combo += 1
                p0 += 1
                p1 += 1
                if p1 == len(arrayList):
                    combo = 0
                    p0 = start0 + 1
                    p1 = p0 + 1
                if p0 == len(arrayList) - 1:
                    return None, None, None
            else:
                p1 += 1
                if p1 == len(arrayList):
                    p0 += 1
                    p1 = p0 + 1
                if p0 == len(arrayList) - 1:
                    return None, None, None
        else:
            if arrayList[p0] == arrayList[p1]:
                combo += 1
                p0 += 1
                p1 += 1
                if p0 == start1:
                    return arrayList[start0:start1], len(arrayList[start0:start1]), start0
                if p1 == len(arrayList):
                    p0 = start0 + 1
                    p1 = p0 + 1
                    combo = 0
            else:
                combo = 0
                p0 = start0
                p1 += 1
                if p1 == len(arrayList):
                    p0 += 1
                    p1 = p0 + 1


if __name__ == '__main__':
    array1 = b'asdf012345601234560123456'
    print("The text is {}".format(array1))
    block, block_size, offset = find_repeat(bytearray(array1))
    print("with repeat block {} \nwith block size {} "
          "\nwith offset {}\n ====== \n\n".format(block, block_size, offset))

    array2 = b'This 1s non-repeat something that magic???what??'
    print("The text is {}".format(array2))
    block, block_size, offset = find_repeat(bytearray(array2))
    print("with repeat block {} \nwith block size {} "
          "\nwith offset {}\n ====== \n\n".format(block, block_size, offset))

    # random tests
    iteration = 0
    max_iter = 1

    while iteration <= max_iter:
        iteration += 1
        N = random.randint(10, 65)
        magic_text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        magic_text = magic_text.encode('utf-8')
        print("The text is {}".format(magic_text))
        block, block_size, offset = find_repeat(bytearray(magic_text))
        print("with repeat block {} \nwith block size {} "
              "\nwith offset {}\n ====== \n\n".format(block, block_size, offset))

    print("Testing the get_block()")
    print("The result of get_block block_size=5, offset=3 for array {}".format(array1))
    print(get_block(array1, 5, 3))





