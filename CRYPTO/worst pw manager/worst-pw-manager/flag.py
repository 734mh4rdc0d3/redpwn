import os
import string
import itertools
passwords = {}

def definepasswords():
	for file in os.listdir("./passwords/"):
		filename = file
		idx, mask = filename.split("_")
		mask = mask[:-4]
		with open("./passwords/"+file, "rb") as f:
			pwd = f.read()
			passwords[idx] = {"mask": mask , "pass": pwd}

def pwcandidates(mask):
	candidates = set()
	#135791
	ub = 2**len(mask)
	form = "{:0"+str(len(mask))+"b}"
	for i in range(ub):
		pw = ""
		orientation = list(form.format(i))
		for index in range(len(orientation)):
			if(mask[index] in string.ascii_lowercase):
				# ( ( (c - ord("a") + i) % 26) + ord("a") )
				if(orientation[index] == "0"):
					#normal
					pw += chr( (ord(mask[index]) - ord("a") - index)%26 + ord("a"))
					pass
				else:
					#reverse mod
					pw += chr( (ord(mask[index]) - ord("a") + 26 - index)%26 + ord("a"))
			else:
				# ( ( (c - ord("0") + i) % 10) + ord("0") )
				if(orientation[index] == "0"):
					#normal
					pw += chr( (ord(mask[index]) - ord("0") - index)%10 + ord("0") )
				else:
					#reverse mod
					pw += chr( (ord(mask[index]) - ord("0") + 10 - index)%10 + ord("0") )
		candidates.add(pw)
	return list(candidates)

def guessallpwcandidates():
	for k in passwords.keys():
		passwords[k]["pwcandidate"] = pwcandidates(passwords[k]["mask"])[0]
		#print(passwords[k])

class KeyByteHolder():
	def __init__(self, num):
		assert num >= 0 and num < 256
		self.num = num

	def __repr__(self):
		return hex(self.num)[2:]

def rc4(text, key): # definitely not stolen from stackoverflow
	S = [i for i in range(256)]
	j = 0
	out = bytearray()
	#KSA Phase
	for i in range(256):
		j = (j + S[i] + key[i % len(key)].num) % 256
		S[i] , S[j] = S[j] , S[i]

	#PRGA Phase
	i = j = 0
	for char in text:
		i = ( i + 1 ) % 256
		j = ( j + S[i] ) % 256
		S[i] , S[j] = S[j] , S[i]
		out.append(ord(char) ^ S[(S[i] + S[j]) % 256])
	return out

def bruteAllRC4():
	for k in passwords.keys():
		for i in range(256):
			key = [KeyByteHolder(i)] * 8
			guess = rc4(passwords[k]['pwcandidate'] , key)
			if(guess == passwords[k]['pass']):
				passwords[k]['flagkey'] = chr(i)
				#print(passwords[k])
				break

definepasswords()
guessallpwcandidates()
bruteAllRC4()

for i in range(10, 100):
	flagcandidate = ["#"]*i
	place = 0
	for j in range(410):
		place = (place+8)%i
		if(str(j) in passwords.keys()):
			if(flagcandidate[place] == "#"):
				flagcandidate[place] = passwords[str(j)]['flagkey']
			else:
				if(flagcandidate[place] != passwords[str(j)]['flagkey']):
					break
	print(i , "".join(flagcandidate))