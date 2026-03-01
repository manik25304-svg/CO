def rtypr(x):
    arr=[]
    if(x=="sltu"):
        arr.append("0000000")
        arr.append("011")              # type of arr-> func7 , func3 , opcode
        arr.append("0110011")
    elif (x=="xor"):
        arr.append("0000000")
        arr.append("100")              
        arr.append("0110011")

def stype(x):
    arr=[]
    if (x=="sw"):           # type of arr-> func3 , opcode
        arr.append("010")              
        arr.append("0100011")

def btype(x):
    arr=[]
    if (x=="beq"):           # type of arr-> func3 , opcode
        arr.append("000")              
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
def utype(x):
    arr=[]
    if (x=="lui"):             
        arr.append("0110111")
    elif (x=="auipc"):             
        arr.append("0010111")


n=input.split()
