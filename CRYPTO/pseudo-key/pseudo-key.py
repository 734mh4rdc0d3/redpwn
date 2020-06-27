from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}
#chr_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
#num_to_chr = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def encrypt(ptxt, key):
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

with open('flag.txt') as f, open('key.txt') as k:
	flag = f.read()
	key = k.read()

ptxt = flag[5:-1]

ctxt = encrypt(ptxt,key)
pseudo_key = encrypt(key,key)

print('Ciphertext:',ctxt)
print('Pseudo-key:',pseudo_key)
