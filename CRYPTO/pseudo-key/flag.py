from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

#chr_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
#num_to_chr = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

ciphertext= "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"
pseudokey=  "iigesssaemk"
#pseudokey = "iig"

def decrypt(ctxt , key):
	ctxt = ctxt.lower()
	key = ''.join(key[i % len(key)] for i in range(len(ctxt))).lower()
	ptxt = ''
	for i in range(len(ctxt)):
		if ctxt[i] == '_':
			ptxt += '_'
			continue
		x = chr_to_num[ctxt[i]]
		y = chr_to_num[key[i]]
		ptxt += num_to_chr[(x - y) % 26]
	return ptxt

def generatekeys(key):
	keys= list()
	form = "0"+str(len(key))+"b"
	#possible combinations 2^len(key)
	for i in range(2**len(key)):
		t = list(format(i,form))
		k = ""
		try:
			for j in range(len(t)):
				if(t[j] == '0'): #normal decryption
					k += num_to_chr[chr_to_num[key[j]]/2]
				else:
					k += num_to_chr[(26+chr_to_num[key[j]])/2]
			keys.append(k)
		except:
			continue
	return keys

allkeys = generatekeys(pseudokey)
for k in allkeys:
	print(k , decrypt(ciphertext, k))