ciphertext = "0111001001001100101100011101000011010010010110110001111100001001110001001000110011110011100100000001101100000001001101001101010111010000111101000011100100001000100001000100000100000100010101001111001011100110100000000001100100101000011110001001010111000001000001110000001111010001000000000110100101010"

def bit_str_xor(bit_str_1, bit_str_2):
	xor_res = ''
	for i in range(len(bit_str_1)):
		bit_1 = bit_str_1[i]
		bit_2 = bit_str_2[i]
		xor_res += str(int(bit_1) ^ int(bit_2))
	return xor_res

flag = ""
while(True):
	print(flag)
	choice = int(input("how many characters to brute(even number):"))
	part = ciphertext[:7*choice]
	ciphertext = ciphertext[7*choice:]
	candidates = {}
	bound = str(int(7*choice/2))
	form = "{:0"+ bound +"b}"
	file = open("output.txt" , "w")
	for i in range(2**int(bound)):
		seq = list(form.format(i))
		randseq = ""
		for num in seq:
			if(num == "0"):
				randseq += "10"
			else:
				randseq += "11"
		result = bit_str_xor(randseq , part)
		chars = ""
		found = False
		for _ in range(choice):
			temp = int(result[:7] ,2)
			if(temp > 94 and temp < 126):
				chars += chr(temp)
				result = result[7:]
			else:
				found = True
				break
		if(found):
			continue
		candidates[i] = chars
		file.write(str(str(i) +",  " + flag+chars+ "\n"))
	file.close()
	choice = int(input("enter int i corresponding the chars to append to the flag: "))
	flag += candidates[choice]

