import re
def rval(a):
    rd=format(a,'05b')
    return str(rd)
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
#can i define a funtion such taht it will give me a method to read lines one by on
def j_jumper(pc,label,labelname):
    a=label[labelname]
    pc=a
    return pc
def j_type(x,pc,ra,label):
    #to find the immediate value string
    imm=label[x[2]]-pc
    imm1=format(imm & 0xfffff,'020b')
    #imm2=format(imm & 0xffffffff,'032b')
    #imm[20|10 : 1|11|19 : 12] rd opcode J-type
    ra=hex(pc+4)
    pc=hex(pc+imm)
    imm3=imm1[0]+imm1[10:20]+imm1[9]+imm1[1:9]
    #imm[20|10 : 1|11|19 : 12] rd 1101111 jal
    rd=rval(reg[x[1]])
    opcode="1101111"
    inst=imm3+rd+opcode
    return ra,pc,inst






    




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
            #here the value of pc place will be up for variation based on the number of codelines that will occur in this
            address_inst[hex(pc_place)]=i
            pc_place+=4
        for j in address_inst:
            inst2=address_inst[j]
            if inst2[0][-1]==":":
                label[inst2[0]]=j
        returnaddresses=[]


except FileNotFoundError:
    print(f"Error: The file '{inst_set}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

