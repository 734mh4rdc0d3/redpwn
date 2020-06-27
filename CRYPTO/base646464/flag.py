import base64
cipher = open("cipher.txt" , 'r')

ciphertext = cipher.read()
for i in range(25):
	ciphertext = base64.b64decode(ciphertext)

print(ciphertext.decode("utf-8"))

cipher.close()