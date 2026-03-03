import re

#can i define a funtion such taht it will give me a method to read lines one by on
def j_jumper(pc,label,labelname):
    a=label[labelname]
    pc=a
    return pc

    




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
        

except FileNotFoundError:
    print(f"Error: The file '{inst_set}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
