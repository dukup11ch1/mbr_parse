#-*- coding:utf-8 -*-
import sys
import struct
import codecs

def li2bi(data): return str(struct.pack('>4s', data).encode("hex"))
fp = open("D:\\BoB\\kangdaemyung\\mbr_128.dd","rb")
present=0
present=present+446
fp.seek(present)
a=fp.read(64)
present=present+64
for i in range(0,4):
    print "\npartition "+str(i+1)
    print "active :",
    if a[i*16+0] == "\x00": print "False"
    else: print "True"
    print "CHSaddress1 : 0x"+ li2bi(a[i*16+1:i*16+4]+'\x00')[0:-2]+"(little endian)"
    print "Partition Type : 0x"+li2bi(a[i*16+4]+'\x00'*3)[0:2]
    print "CHSaddress2 : 0x"+li2bi(a[i*16+5:i*16+8]+'\x00')[0:-2]+"(little endian)"
    print "LBAaddress of start: 0x"+li2bi(a[i*16+8:i*16+12])+"(little endian)"
    print "Number of sectors Partition Size : 0x"+li2bi(a[i*16+12:i*16+16])+"(little endian)"
    LBAadderess=struct.unpack("<I",codecs.decode(li2bi(a[i*16+8:i*16+12]),"hex"))[0]
    size=0
    if a[i*16+4]=="\x05":
        while True:
            present=LBAadderess*512
            

