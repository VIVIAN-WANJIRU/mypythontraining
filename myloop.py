ls1 = range(1,20)
ls1 = list(ls1)
print(ls1)

for i in ls1:
    print("i is",i)

# practical example
mydata=["Nrb","Msa","Ksm","Eld","Nkr"]
mydataindexes =list(range(0,len(mydata)))
print(mydataindexes)
for i in list(range(0,len(mydata))):
    if mydata[i] == "Ksm":
       mydata[i] = "Kisumu"  
    else:
        pass
print(mydata)       