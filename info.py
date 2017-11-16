import csv
import math
with open("data.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter='\t')
    my_list = list(reader)
    #print(my_list)
row=len(my_list);
new_l=[];
for j in range(row):
	l=my_list[j][0].split(',');
	new_l.append(l)
print(row);
col=len(new_l[0]);
y_count=0.0;
x_count=0.0;
for i in range(row):
	if(new_l[i][-1]=="yes"):
		y_count+=1;
	else:
		x_count+=1;
ans=0;
print(y_count);
print(x_count);
ans=((y_count/row)*math.log(float(y_count/row))/math.log(2))+((x_count/row)*math.log(float(x_count/row))/math.log(2));
print("Entropy :->");
ans=-1*ans;
print(ans);
d={};
for i in range(row):
	if new_l[i][0] in d:
		d[new_l[i][0]]+=1;
	else:
		d[new_l[i][0]]=1;
print(d);
l=d.keys();
print(l);
d_yes={};
for i in l:
	d_yes[i]=0;
for i in range(row):
	if new_l[i][-1]=="yes":
		d_yes[new_l[i][0]]+=1;
ans1=0;
for i in l:
	ans1+=-1*(((d_yes[l]/d[l])*math.log(float(d_yes[l]/d[l])))/math.log(2))+(((d[l]-d_yes[l])/d[l])*math.log(float((d[l]-d_yes[l])/d[l]))/math.log(2)));
print(ans1);


			 
	
	


