import sys


fp = open("mbr_128.dd","rb")
present=0
while True:
    present=present+446
    fp.seek(present)
    a=fp.read(64)
    present=present+64
    a=list(a)
    if a[0]==
