string ='lalan'
dict={}

for n in string:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
print (dict)
stry=""
keys=dict.keys()
print (keys)
# values=dict.values()
# j=0
for i in keys :
    print(i)
    stry+=str(dict[i])+i
print (stry)