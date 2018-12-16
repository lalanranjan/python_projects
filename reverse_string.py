txt='lalanranjan'
newtxt=''
for i in range (len(txt)):
    m=txt[i]
    newtxt=m+newtxt
print (newtxt)
List = []
List.append("".join(reversed(txt)))
print (List[0])
print("123".join(reversed(txt)))