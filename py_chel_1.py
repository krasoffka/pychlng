s ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

z = 'map'
x = []
for ch in z:
    if 96 < ord(ch) < 120:
        x.append(chr(ord(ch) + 2))
    elif ord(ch) > 120:
        x.append(chr(ord(ch) + 98 - 122))
    else:
        x.append(ch)

# print(ord('a'))
# print(ord('z'))
# print(ord(' '))
# print(ord('|'))

x = ''.join(x)


print(x)

'''i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's
why this text is so long. using string.maketrans() is recommended. now apply on the url.'''


