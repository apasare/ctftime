#!/usr/bin/env python3

from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}


def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
    return ctxt


def decrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(26 + x - y) % 26]
    return ctxt


def decrypt_key(ctxt):
    ptxt = ''
    for i in range(len(ctxt)):
        x = chr_to_num[ctxt[i]]
        ptxt += num_to_chr[((26 + x)/2) % 26]
    return ptxt


key = "iigesssaemk"
print(decrypt_key(key))
key = "redpwwwnctf"
print(decrypt("z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut", key))


# with open('flag.txt') as f, open('key.txt') as k:
#     flag = f.read()
#     key = k.read()

# ptxt = flag[5:-1]

# ctxt = encrypt(ptxt,key)
# pseudo_key = encrypt(key,key)

# print('Ciphertext:',ctxt)
# print('Pseudo-key:',pseudo_key)
