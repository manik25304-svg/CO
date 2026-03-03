import re

#can i define a funtion such taht it will give me a method to read lines one by on
def j_jumper(pc,label,labelname):
    a=label[labelname]
    pc=a
    return pc
def utype(x):
    arr=[]
    if (x=="lui"):             
        arr.append("0110111")
    elif (x=="auipc"):             
        arr.append("0010111")
    return arr
def rval(a):
    rd=format(a,'05b')
    return str(rd)
def btype(x):
    arr=[]
    if(x=="beq"):
        arr.append("000")              # type of arr-> func3 , opcode
        arr.append("1100011")
    elif (x=="bne"):
        arr.append("001")              
        arr.append("1100011")
    elif (x=="blt"):
        arr.append("100")              
        arr.append("1100011")
    elif (x=="bge"):
        arr.append("101")              
        arr.append("1100011")
    elif (x=="bltu"):
        arr.append("110")              
        arr.append("1100011")
    elif (x=="bgeu"):
        arr.append("111")              
        arr.append("1100011")
    return arr
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
        arr.append("0100000")
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
    "x10":10, "a0":10,          # acesss register based on given value
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
ity=["lw","addi","sltiu","jalr"]
s=["sw"]
b=["beq","bne","blt","bge","bltu","bgeu"]
u=["lui","auipc"]
jtyp=["jal"]


inst_set = input("Enter the file you want to run on assembler: ")

try:
    with open(inst_set, 'r') as f:
        instructions = f.readlines()
        pc_place= 0x1000
        label={}
        address_inst={}
        #Now a block will be defined to do a framework regarding each value in it
        for i in instructions:
            inst=re.split(r'[,()\s]+',i)
            inst = [x for x in inst if x]
            #here the value of pc place will be up for variation based on the number of codelines that will occur in this
            address_inst[hex(pc_place)]=inst
            pc_place+=4
        pc_place=0x1000
        for j in address_inst.values():
            
            inst2=j
            if inst2[0][-1]==":":
                label[inst2[0]]=pc_place
            pc_place+=4

        for x in address_inst:
            
            inst2=address_inst[x]
            pos=0
            if inst2[0][-1]==":":
                pos=1
            if(inst2[pos] in r):
                a=rtype(inst2[pos])
                rs2=rval(reg[inst2[pos+3]])
                rs1=rval(reg[inst2[pos+2]])
                rd=rval(reg[inst2[pos+1]])
                print(a[0]+rs2+rs1+a[1]+rd+a[2])
            elif(inst2[pos] in ity):
    
                if(inst2[pos]=="lw"):
                    rs1=inst2[pos+3]
                    rs1=rval(reg[rs1])
                    rd=inst2[pos+1]
                    rd=rval(reg[rd])
                    imm = int(inst2[pos+2])
                    imm = format(imm & 0xfff, '012b')
                    imm=str(imm)
                    opcode="0000011"
                    func3="010"
                    print(imm+rs1+func3+rd+opcode)
                elif(inst2[pos]=="addi" or inst2[pos]=="sltiu" or inst2[pos]=="jalr"):    
                    imm = int(inst2[pos+3])
                    imm = format(imm & 0xfff, '012b')
                    imm=str(imm)
                    rs1=rval(reg[inst2[pos+2]])
                    rd=rval(reg[inst2[pos+1]])
                    if(inst2[pos]=="addi"):
                        opcode="0010011"
                        func3="000"
                        print(imm+rs1+func3+rd+opcode)
                    elif(inst2[pos]=="sltiu"):
                        opcode="0010011"
                        func3="011"
                        print(imm+rs1+func3+rd+opcode)
                    elif(inst2[pos]=="jalr"):
                        opcode="1100111"
                        func3="000"
                        print(imm+rs1+func3+rd+opcode)
            elif(inst2[pos+0] in s):
                if(inst2[pos+0]=="sw"):
                    imm=int(inst2[pos+2])
                    imm = format(imm & 0xfff, '012b')
                    imm=str(imm)
                    rs2=rval(reg[inst2[pos+1]])
                    rs1=rval(reg[inst2[pos+3]])
                    func3="010"
                    opcode="0100011"
                    print(imm[0:7]+rs2+rs1+func3+imm[7:12]+opcode)
            elif(inst2[pos+0] in u):
                a=utype(inst2[pos+0])
                rd=rval(reg[inst2[pos+1]])
                imm=int(inst2[pos+2])
                imm=imm//4096
                imm = format(imm & 0xfffff , '020b')
                imm=str(imm)
                print(imm+rd+a[0])
            elif(inst2[pos] in b):
                a=btype(inst2[pos])
                rs1=rval(reg[inst2[pos+1]])
                rs2=rval(reg[inst2[pos+2]])
                imm=inst2[pos+3]
                pc=int(x,16)
                if imm.isdigit():
                    imm=int(imm)
                else:
                    imm=label[imm+":"]-pc
                imm = format(imm & 0x1fff , '013b')
                print(imm[0]+imm[2:8]+rs2+rs1+a[0]+imm[8:12]+imm[1]+a[1])
            elif(inst2[pos] in jtyp):
                if inst2[pos] == "jal":
                    opcode="1101111"
                    rd=rval(reg[inst2[pos+1]])
                    imm = inst2[pos+2]
                    pc = int(x, 16)
                    if imm.isdigit():
                        imm=int(imm)
                    else:
                        imm = label[imm+":"] - pc
                    imm = format(imm & 0x1fffff, '021b')

                    print(imm[0]+imm[10:20]+imm[9]+imm[1:9]+rd+opcode)

            
            



        

except FileNotFoundError:
    print(f"Error: The file '{inst_set}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
