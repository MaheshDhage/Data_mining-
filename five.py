print("Enter number of data")
n=input()
n=int(n);
l=[]
for i in range(n):
    l.append(int(input()));
l.sort();
q1=int(n/4);
q2=int(n/2);
q3=3*int(n/4);
if(n%2==0):
    mid=int(n/2)
    q2=(l[mid-1]+l[mid])/2;
    if(mid%2):
        mmid=int(mid/2);
        q1=(l[mmid-1]+l[mmid])/2
    else:
        omid=int(mid/2);
        q1=l[omid];
    q3mmid=int(n*3/4)
    print("Q_3 mid")
    print(q3mmid);
    if((n*3/4)==0):
        q3=(l[q3mmid-1]+l[q3mmid])/2
    else:
        q3=l[q3mmid];
else:
    mid=int(n/2)
    q2=(l[mid]);
    if(mid%2==0):
        mmid=int(mid/2);
        q1=(l[mmid-1]+l[mmid])/2
    else:
        omid=int(mid/2);
        q1=l[omid];
    q3mmid=int(n*3/4)
    if((n*3/4)==0):
        q3=(l[q3mmid-1]+l[q3mmid])/2
    else:
        q3=l[q3mmid];
print("Min--> ")
print(l[0])
print("Max--> ")
print(l[-1])
print("Q1--> ")
print(q1)
print("Q2--> ")
print(q2)
print("Q3--> ")
print(q3)
