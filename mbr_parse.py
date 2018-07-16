#-*- coding:utf-8 -*-
import sys
import struct
import codecs

def li2bi(data): return struct.unpack("<I",codecs.decode(str(struct.pack('>4s', data).encode("hex")),"hex"))[0]#little endian

fp = open("../mbr_128.dd","rb")#파일 오픈

fp.seek(446)#시작지점 정하기
a=fp.read(64)#64byte읽음
partition=1#파티션
for i in range(0,4):
    print "\npartition "+str(partition)#몇번째 파티션?
    partition = partition+1
    print "active :",
    if a[i*16+0] == "\x00": print "False"#00이면 부팅이 안됨(80일때만 가능)
    else: print "True"
    print "CHSaddress1 : "+ str(hex(li2bi(a[i*16+1:i*16+4]+'\x00')))+"(big endian)"
    print "Partition Type : "+str(hex(li2bi(a[i*16+4]+'\x00'*3)))
    print "CHSaddress2 : "+str(hex(li2bi(a[i*16+5:i*16+8]+'\x00')))+"(big endian)"
    print "LBAaddress of start: "+str(hex(li2bi(a[i*16+8:i*16+12])))+"(big endian)"
    print "Number of sectors Partition Size : "+str(hex(li2bi(a[i*16+12:i*16+16])))+"(big endian)"
    
    
    
    if a[i*16+4]=="\x05":#ebr일 경우
        baseadress=li2bi(a[i*16+8:i*16+12])
        present=baseadress*512+446
        break1=False
        while True:
            fp.seek(present)
            if break1:
                break
            fnext=fp.read(32)
            if fnext[24:28]=="\x00\x00\x00\x00":
                break1=True
            print "\npartition "+str(partition)+"(EBR)"
            partition=partition+1
            print "active :",
            if fnext[0] == "\x00": print "False"
            else: print "True"
            print "CHSaddress1 : "+ str(hex(li2bi(fnext[1:4])))+"(big endian)"
            print "Partition Type : "+str(hex(li2bi(fnext[4])))
            print "CHSaddress2 : "+str(hex(li2bi(fnext[5:8])))+"(big endian)"
            print "LBAaddress of start: "+str(hex(li2bi(fnext[8:12])))+"(big endian)"
            print "Real address : "+str(hex(present-446))+"(big endian)"
            print "Number of sectors Partition Size : "+str(hex(li2bi(fnext[12:16])))+"(big endian)"
            LBAaddress=li2bi(fnext[24:28])
            present=(baseadress+LBAaddress)*512+446
            
