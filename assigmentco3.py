import re
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
def b_type(arr):
    inst=arr[0]
    rs1=arr[1]
    rs2=arr[2]
    imm=arr[3]
    imm1=imm[0]+imm[2:7]
    imm2=imm[8:11]+imm[1]
    opcode="1100011"
    output_str=""
    if inst=="beq":
        output_str=imm1+rs2+rs1+"000"+imm2+opcode
        return output_str
    elif inst=="bne":
        output_str=imm1+rs2+rs1+"001"+imm2+opcode
        return output_str
    elif inst=="blt":
        output_str=imm1+rs2+rs1+"100"+imm2+opcode
        return output_str
    elif inst=="bge":
        output_str=imm1+rs2+rs1+"101"+imm2+opcode
        return output_str
    elif inst=="bltu":
        output_str=imm1+rs2+rs1+"110"+imm2+opcode
        return output_str
    elif inst=="bgeu":
        output_str=imm1+rs2+rs1+"111"+imm2+opcode
        return output_str
def j_type(arr):
    inst=arr[0]
    rd=arr[1]
    imm=arr[2]
    imm1=imm[0]+imm[10:19]+imm[9]+imm[1:8]
    opcode="1101111"
    outputstr=""
    if inst=="jal":
        outputstr=imm1+rd+opcode
        return outputstr



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
elif(ip[0] in i):
    rs1=ip[2]
    rs1=format(reg[rs1],'05b')
    rs1=str(rs1)
    rd=ip[1]
    rd=format(reg[rd],'05b')
    rd=str(rd)
    imm = int(ip[3])
    imm = format(imm & 0xfff, '012b')
    imm=str(imm)
    if(ip[0]=="lw"):
        rs1=ip[3]
        rs1=format(reg[rs1],'05b')
        rs1=str(rs1)
        rd=ip[1]
        rd=format(reg[rd],'05b')
        rd=str(rd)
        imm = int(ip[2])
        imm = format(imm & 0xfff, '012b')
        imm=str(imm)
        opcode="0000011"
        func3="010"
        print(imm+rs1+func3+rd+opcode)
        
    elif(ip[0]=="addi"):
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

    




    

    
