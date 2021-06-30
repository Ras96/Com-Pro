import random

def _en(c, p):
    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') + p) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') + p) % 26 + ord('a'))

    return c

def en(s):
    # p = random.randint(1, 25)
    # q = random.randint(1, 10)
    p = 2
    q = -8
    cipher = ''
    for c in s:
        cipher += _en(c, p)
        p += q
    return cipher

def main():
    flag = "DROC{DupNgM_HMz_ew_XkpX1kK1z_PS_lGKv}"
    print(en(flag))

if __name__ == '__main__':
    main()