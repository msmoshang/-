#0b二进制 0o八进制 0x十六进制
print ("1:10转2,8,16\n2:2转8,10,16\n3:8转2,10,16\n4:16转2，8，10")
c = int( input("请输入一个数字:"))

if c == 1:
    a = int(input("请输入你想转换的十进制:" ))
    print ("二进制为:",bin(a)[2:])
    print ("八进制为:",oct(a)[2:])
    print ("十六进制为:",hex(a)[2:])
elif c == 2:
    b = int(input("请输入一个二进制:"))
    print ("八进制为:",oct(int(str(b),2))[2:])
    print ("十进制为:",int(str(b),2))
    print ("十六进制为:",hex(int(str(b),2))[2:])
elif c == 3:
    d = int(input("请输入一个八进制:"))
    print ("二进制为:",bin(int(str(d),8))[2:])
    print ("十进制为:",int(str(d),8))
    print ("十六进制为:",hex(int(str(d),8))[2:])
      
elif c == 4:
    e = (input("请输入一个十六进制的数:"))
    print ("二进制为:",bin(int(str(e),16)))
    print ("八进制为:",oct(int(str(e),16)))
    print ("十进制为:",str(int(str(e),16)))
