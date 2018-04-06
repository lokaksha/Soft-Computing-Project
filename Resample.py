import numpy as np
import math
import random

print "Enter learning rate :",
l=input()

def sigmoid(s):
	if s <= -700:
		return 0
	res=1/(1+math.exp(-s))
	return res

file=open("chronic_kidney_disease.arff","r")
a=[]
i=-29
for x in file:
	if i < 0:
		i+=1
	else:
		(b)=x.split(",")
		a.append(b)

for i in range(400):
	if a[i][5]=="normal":
		a[i][5]=0
	if a[i][5]=="abnormal":
		a[i][5]=1

	if a[i][6]=="normal":
		a[i][6]=0
	if a[i][6]=="abnormal":
		a[i][6]=1

	if a[i][7]=="present":
		a[i][7]=0
	if a[i][7]=="notpresent":
		a[i][7]=1

	if a[i][8]=="present":
		a[i][8]=0
	if a[i][8]=="notpresent":
		a[i][8]=1

	if a[i][18]=="yes":
		a[i][18]=0
	if a[i][18]=="no":
		a[i][18]=1

	if a[i][19]=="yes":
		a[i][19]=0
	if a[i][19]=="no":
		a[i][19]=1

	if a[i][20]=="yes":
		a[i][20]=0
	if a[i][20]=="no":
		a[i][20]=1

	if a[i][21]=="good":
		a[i][21]=0
	if a[i][21]=="poor":
		a[i][21]=1

	if a[i][22]=="yes":
		a[i][22]=0
	if a[i][22]=="no":
		a[i][22]=1

	if a[i][23]=="yes":
		a[i][23]=0
	if a[i][23]=="no":
		a[i][23]=1

	if a[i][24]=="ckd\n":
		a[i][24]=0
	if a[i][24]=="notckd\n":
		a[i][24]=1

for i in range(400):
	for j in range(25):
		if a[i][j]!="?":
			a[i][j]=float(a[i][j])

for j in range(9,18):
	x=0.0
	y=0.0
	xn=0
	yn=0
	for i in range(400):
		if a[i][24]==1 and a[i][j]!="?":
			x+=a[i][j]
			xn+=1
		if a[i][24]==0 and a[i][j]!="?":
			y+=a[i][j]
			yn+=1
	for i in range(400):
		if a[i][24]==1 and a[i][j]=="?":
			a[i][j]=x/xn
		if a[i][24]==0 and a[i][j]=="?":
			a[i][j]=y/yn

for i in range(400):
	if a[i][2]=="?":
		if a[i][24]==1:
			a[i][2]=1.020
		if a[i][24]==0:
			a[i][2]=1.015

for i in range(400):
	if a[i][3]=="?":
		if a[i][24]==1:
			a[i][3]=0
		if a[i][24]==0:
			a[i][3]=2

for i in range(400):
	if a[i][4]=="?":
		if a[i][24]==1:
			a[i][4]=0
		if a[i][24]==0:
			a[i][4]=1

#0-143 1-9 => "?"
for i in range(400):
	if a[i][5]=="?":
		if a[i][24]==1:
			a[i][5]=0
		if a[i][24]==0:
			a[i][5]=1

for i in range(400):
	if a[i][6]=="?":
		if a[i][24]==1:
			a[i][6]=0
		if a[i][24]==0:
			a[i][6]=1

for i in range(400):
	if a[i][7]=="?":
		if a[i][24]==1:
			a[i][7]=1
		if a[i][24]==0:
			a[i][7]=0

for i in range(400):
	if a[i][8]=="?":
		if a[i][24]==1:
			a[i][8]=1
		if a[i][24]==0:
			a[i][8]=0

for j  in range(25):
	max=0
	for i in range(400):
		if a[i][j]>max:
			max=a[i][j]
		if a[i][j]<min:
			min=a[i][j]
	max=max/5
	if max > 10:
		for i in range(400):
			a[i][j]=(a[i][j])/(max)

for i in range(100):
	y=[]
	x=random.randint(250,399)
	for j in range(25):
		y.append(a[x][j])
	a.append(y)

#print data set
# for i in range(500):
# 	print i,
# 	for j in range(25):
# 		print a[i][j],
# 	print ""

actual_class=[]
for i in range(500):
	actual_class.append(a[i].pop(24))

# Data set complete
# 12 nodes in hidden layer

w=[]
for i in range(12):
	temp=[]
	for j in range(24):
		temp.append(1.0*random.randint(-100,100)/100)
	w.append(temp)

wo=[]
for i in range(12):
	wo.append(1.0*random.randint(-100,100)/100)

b=[]
for i in range(12):
	b.append(1.0*random.randint(-100,100)/100)

bo=1.0*random.randint(-100,100)/100

err=[]
for i in range(12):
	err.append(0)

for count in range(160):
	for x in range(500):
		if x%10 != count%10:
			o= np.dot(w,a[x])+b
			for i in range(12):
				o[i]= sigmoid(o[i])

			o1=sigmoid(np.dot(wo,o)+bo)
			
			e=o1*(1-o1)*(actual_class[x]-o1)

			for i in range(12):
				err[i]=o[i]*(1-o[i])*e*wo[i]

			for i in range(12):
				wo[i]+=l*e*o[i]

			for i in range(12):
				for j in range(24):
					w[i][j]+=l*err[i]*a[x][j]

			bo+=l*e

			for i in range(12):
				b[i]+=l*err[i]
	for x in range(500):
		if x%10 == count%10:
			o= np.dot(w,a[x])+b
			for i in range(12):
				o[i]= sigmoid(o[i])

			o1=sigmoid(np.dot(wo,o)+bo)
			if o1<0.5:
				ans=0
			else:
				ans=1
			# print ans,actual_class[x],o1

#RESULTS
tp=tn=fp=fn=0
rmse=0.0
for x in range(500):
	o=np.dot(w,a[x])+b
	for i in range(12):
		o[i]=sigmoid(o[i])
	o1=sigmoid(np.dot(wo,o)+bo)
	if o1 >= 0.5 and actual_class[x]==1:
		tp+=1
	if o1 >= 0.5 and actual_class[x]==0:
		fp+=1
		rmse+=1
	if o1 < 0.5 and actual_class[x]==0:
		tn+=1
	if o1 < 0.5 and actual_class[x]==1:
		fn+=1
		rmse+=1

rmse=1.0*(rmse/300)**0.5
print tp,fp
print tn,fn

print "Learning rate",l
print "Precision",1.0*tp/(tp+fp)
print "Recall",1.0*tp/(tp+fn)
print "F-Measure",2.0*tp/(2*tp+fp+fn)
print "RMSE",rmse