print("Enter bin size:->");
n=int(input());
l=[];
for i in range(n):
    l.append(int(input()));
l.sort();
size=len(l);
sum=0;
for i in l:
    sum=sum+i;
m=(sum/len(l));
sd=0;
for i in l:
    sd=sd+(i-m)**2;
sd=sd/(len(l)-1);
sd=(sd**(1/2))
for i in l:
    print((i-m)/sd);

