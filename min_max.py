print("Enter bin size:->");
n=int(input());
l=[];
for i in range(n):
    l.append(int(input()));
l.sort();
size=len(l);
sum=0;
print("new max:->");
n_max=int(input());
print("new min:->");
n_min=int(input());
bins4=[];
for i in l:
    bins4.append((n_max-n_min)*(1.0*(i-l[0])/(l[-1]-l[0])));
print(bins4);

