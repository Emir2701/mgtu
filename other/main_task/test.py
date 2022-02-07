from8 = {'0':'000','1':'001','2':'010','3':'011',\
         '4':'100','5':'101','6':'110','7':'111'}

to16 = {'0000':'0', '0001':'1', '0010':'2', '0011':'3',\
        '0100':'4', '0101':'5', '0110':'6', '0111':'7',\
        '1000':'8', '1001':'9', '1010':'A', '1011':'B',\
        '1100':'C', '1101':'D', '1110':'E', '1111':'F'}

f_in = open("in.txt","r")
for st in f_in:
    # 1 - to bin
    st = st.strip()
    print('oct: ',st)
    binst = ''
    for el in st:
        if el == '.':
            binst = binst + '.'
        else:
            binst = binst + from8[el]
    print('bin: ', binst)

    # 2 - to hex
    # normal
    ibinst, fbinst = binst.split('.')
    ibinst = '0'*(4 - len(ibinst)%4) + ibinst
    fbinst = fbinst + '0'*(4 - len(fbinst)%4)
    binst = ibinst + '.' + fbinst
    
    # to hex
    res = ''
    pos = 0
    while pos < len(binst):
        if binst[pos] == '.':
            res += '.'
            pos += 1
        else: 
            cur = binst[pos:pos+4]
            res += to16[cur]
            pos += 4
    print('hex: ', res)
    print()
    
f_in.close()
