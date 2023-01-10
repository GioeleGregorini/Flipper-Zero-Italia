import binascii, hashlib, re, sys

uidre = re.compile('^04[0-9a-f]{12}$', re.IGNORECASE)
magic_nums = [3, 5, 7, 23, 9985861487287759675192201655940647, 38844225342798321268237511320137937]

def calc_keya(uid, sector):
    if uidre.match(uid) is None:
        raise ValueError('invalid UID (seven hex bytes)')

    if sector < 0 or sector > 4:
        raise ValueError('invalid sector (0-4)')

    PRE = format(magic_nums[0] * magic_nums[1] * magic_nums[3] * magic_nums[5], '032x')
    POST = format(magic_nums[0] * magic_nums[2] * magic_nums[4], '030x')

    sha1 = hashlib.sha1()
    sha1.update(binascii.unhexlify(PRE + uid + POST))
    key = sha1.digest()

    return binascii.hexlify(key[3::-1] + key[7:5:-1])

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == '-eml':
        keys = calc_keya(sys.argv[1], 0)
        print ('0'*8+keys+'\n'+('0'*32+'\n')*3).join([keys]*5).join([(sys.argv[1]+'0'*18+'\n')+(('0'*32+'\n')*2),'0'*8+keys])
    elif len(sys.argv) > 1:
        print (calc_keya(sys.argv[1], 0))