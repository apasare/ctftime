# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.5.2 (default, Oct  7 2020, 17:19:02) 
# [GCC 5.4.0 20160609]
# Embedded file name: ./script.py
# Compiled at: 2020-12-12 13:17:01
# Size of source mod 2**32: 481 bytes
import base64
secret = 'https://google.com'
cipher2 = [b'NDE=', b'NTM=', b'NTM=', b'NDk=', b'NTA=', b'MTIz', b'MTEw', b'MTEw', b'MzI=', b'NTE=', b'MzQ=', b'NDE=', b'NDA=', b'NTU=', b'MzY=', b'MTEx', b'NDA=', b'NTA=', b'MTEw', b'NDY=', b'MTI=', b'NDU=', b'MTE2', b'MTIw']
cipher1 = [base64.b64encode(str(ord(i) ^ 65).encode()) for i in secret]
m = [chr(int(base64.b64decode(i).decode()) ^ 65) for i in cipher2]
print(''.join(m))
# okay decompiling __pycache__/script.cpython-38.pyc
