print("Enter bin size:->");
n=int(input());
l=[];
for i in range(n):
    l.append(int(input()));
l.sort();
size=len(l);
print("Enter Number of bin's:->");
m=int(input());
bins=[];
tmp=[];
i=0;
print("Equi width:>");
while(i<len(l)):
    tmp=[];
    for j in range(int(n/m)):
        tmp.append(l[i]);
        i+=1;
    bins.append(tmp);
print(bins);

print("Bin boundry:>");
bins2=[];
for i in bins:
    tmp=[];
    for j in i:
        if(abs(j-i[0])<abs(j-i[-1])):
            tmp.append(i[0]);
        else:
            tmp.append(i[-1]);
    bins2.append(tmp);
print(bins2);
print("Bin By mean:->")
bins=[];
for i in bins:
    tmp=[];
    for j in i:
            tmp.append(1.0*(sum(i)/len(i)));
    print
    bins.append(tmp);
print(bins);

