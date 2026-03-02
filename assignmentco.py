import re
def rval(a):
    rd=format(a,'05b')
    return str(rd)

def rtype(x):
    arr=[]
    if(x=="sltu"):
        arr.append("0000000")
        arr.append("011")              # type of arr-> func7 , func3 , opcode
        arr.append("0110011")
    elif (x=="xor"):
        arr.append("0000000")
        arr.append("100")              
        arr.append("0110011")
    elif (x=="add"):
        arr.append("0000000")
        arr.append("000")              
        arr.append("0110011")
    elif (x=="sub"):
        arr.append("0000000")
        arr.append("000")              
        arr.append("0110011")
    elif (x=="sll"):
        arr.append("0000000")
        arr.append("001")              
        arr.append("0110011")
    elif (x=="slt"):
        arr.append("0000000")
        arr.append("010")              
        arr.append("0110011")
    elif (x=="or"):
        arr.append("0000000")
        arr.append("110")              
        arr.append("0110011")
    elif (x=="srl"):
        arr.append("0000000")
        arr.append("101")              
        arr.append("0110011")
    elif (x=="and"):
        arr.append("0000000")
        arr.append("111")              
        arr.append("0110011")
    return arr
def stype(x):
    arr=[]
    if (x=="sw"):           # type of arr-> func3 , opcode
        arr.append("010")              
        arr.append("0100011")

def utype(x):
    arr=[]
    if (x=="lui"):             
        arr.append("0110111")
    elif (x=="auipc"):             
        arr.append("0010111")


n = input()
ip = re.split(r'[ ,()]', n)
ip = [x for x in ip if x]
reg= {
    "x0":0, "zero":0,
    "x1":1, "ra":1,
    "x2":2, "sp":2,
    "x3":3, "gp":3,
    "x4":4, "tp":4,
    "x5":5, "t0":5,
    "x6":6, "t1":6,
    "x7":7, "t2":7,
    "x8":8, "s0":8, "fp":8,
    "x9":9, "s1":9,
    "x10":10, "a0":10,
    "x11":11, "a1":11,
    "x12":12, "a2":12,
    "x13":13, "a3":13,
    "x14":14, "a4":14,
    "x15":15, "a5":15,
    "x16":16, "a6":16,
    "x17":17, "a7":17,
    "x18":18, "s2":18,
    "x19":19, "s3":19,
    "x20":20, "s4":20,
    "x21":21, "s5":21,
    "x22":22, "s6":22,
    "x23":23, "s7":23,
    "x24":24, "s8":24,
    "x25":25, "s9":25,
    "x26":26, "s10":26,
    "x27":27, "s11":27,
    "x28":28, "t3":28,
    "x29":29, "t4":29,
    "x30":30, "t5":30,
    "x31":31, "t6":31,
}
r=["add","sub","sll","slt","sltu","xor","and","or","srl"]
i=["lw","addi","sltiu","jalr"]
s=["sw"]
b=["beq","bne","blt","bge","bltu","bgeu"]
u=["lui","auipc"]
j=["jal"]

if(ip[0] in r ):
    a=rtype(ip[0])
    rs2=rval(reg[ip[3]])
    rs1=rval(reg[ip[2]])
    rd=rval(reg[ip[1]])
    print(a[0]+rs2+rs1+a[1]+rd+a[2])
elif(ip[0] in i):
    
    if(ip[0]=="lw"):
        rs1=ip[3]
        rs1=rval(reg[rs1])
        rd=ip[1]
        rd=rval(reg[rd])
        imm = int(ip[2])
        imm = format(imm & 0xfff, '012b')
        imm=str(imm)
        opcode="0000011"
        func3="010"
        print(imm+rs1+func3+rd+opcode)
    else:    
        imm = int(ip[3])
        imm = format(imm & 0xfff, '012b')
        imm=str(imm)
        rs1=rval(reg[ip[2]])
        rd=rval(reg[ip[1]])
        if(ip[0]=="addi"):
            opcode="0010011"
            func3="000"
            print(imm+rs1+func3+rd+opcode)
        elif(ip[0]=="sltiu"):
            opcode="0010011"
            func3="011"
            print(imm+rs1+func3+rd+opcode)
        elif(ip[0]=="jalr"):
            opcode="1100111"
            func3="000"
            print(imm+rs1+func3+rd+opcode)
elif(ip[0] in s):
    if(ip[0]=="sw"):
        imm=int(ip[2])
        imm = format(imm & 0xfff, '012b')
        imm=str(imm)
        rs2=rval(reg[ip[1]])
        rs1=rval(reg[ip[3]])
        func3="010"
        opcode="0100011"
        print(imm[0:7]+rs2+rs1+func3+imm[7:12]+opcode)



        
        


