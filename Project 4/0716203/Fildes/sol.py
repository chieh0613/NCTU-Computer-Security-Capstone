from pwn import *

r = remote('140.113.207.240',8831)

r.recvuntil('magic number')
# fd = 0 -> buf = 0xDEADBEAF
r.send(str(0xdeadbeaf))
r.recvuntil('magic string')
# strcmp = 0 to cat the flag -> buf = YOUSHALLNOTPASS
r.sendline('YOUSHALLNOTPASS')
#r.interactive()
print(r.recvall(1))
