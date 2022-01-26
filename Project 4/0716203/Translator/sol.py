
from pwn import *

r = remote('140.113.207.240',8833)

#r.recvline()
r.recvuntil('Give me some input:')
r.sendline('1')
r.recvuntil('translate?')
r.sendline('n')
r.recvuntil('language:')
r.sendline('<6A;')
#r.interactive()
print(r.recvall(1))

