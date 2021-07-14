# Name - Atul Jain 
# Roll No.- B19075

import matplotlib.pyplot as plt
import pandas as pd

# Calculation of Expectation
def expect(e): 
    t=0
    for i in e:
        t+=(i*e[i])
    return t

# Calculation of Variance
def varianc(e,m):
    t=0
    for i in e:
        t+=(i*i*e[i])
    t-=(m*m)
    return t

# Sorting the dictionary and updating it with probabilities
def sortdict(e,t):
    l=list(e.items()) 
    l.sort()
    e=dict(l)
    for i in e:
        e[i]/=t
    return e

# Plotting the PMF
def plotting(dt,case,m,v):
    fig=plt.figure()
    a=dt.keys()
    b=dt.values()
    plt.bar(a,b, align='center', alpha=1)
    if(case[0]=='A'):
        plt.xlabel("Age")
    else:
        plt.xlabel("No. of days")
    plt.ylabel("Probability")
    q=case
    plt.title(q)
    plt.show()
    print("Expectation =",m)
    print("Variance =",v)
 
# Q1
df=pd.read_excel("Covid19IndiaData_Q1.xlsx")
x=df['Age'].values
y=df['StatusCode'].values
z=df['GenderCode0F1M'].values

r={}
h={}
d={}
dn={}
m={}
f={}

ad=0
bh=0
cr=0
am=0
bf=0

for n in range(0,1315):
    i=x[n]
    j=y[n]
    k=z[n]
    if i in dn:
        dn[i]+=1
    else:
        dn[i]=1
    if(j=="Dead"):
        ad+=1
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    elif(j=="Hospitalized"):
        bh+=1
        if i in h:
            h[i]+=1
        else:
            h[i]=1
    else:
        cr+=1
        if i in r:
            r[i]+=1
        else:
            r[i]=1
    if(k==0):
        bf+=1
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    else:
        am+=1
        if i in m:
            m[i]+=1
        else:
            m[i]=1

dn=sortdict(dn,1315)
dnm=expect(dn)
dnv=varianc(dn,dnm)

r=sortdict(r,cr)
rm=expect(r)
rv=varianc(r,rm)

h=sortdict(h,bh)
hm=expect(h)
hv=varianc(h,hm)

d=sortdict(d,ad)
dm=expect(d)
dv=varianc(d,dm)

m=sortdict(m,am)
mm=expect(m)
mv=varianc(m,mm)

f=sortdict(f,bf)
fm=expect(f)
fv=varianc(f,fm)

# Q1 (a)
print("")
print("Q1 (a) PMF of Patients (Age wise)")
plotting(dn,"Age vs No. of cases for all patients",dnm,dnv)
print("As variance is large, we can say that the data is spread out i.e. covid is present in a lot of age groups")

# Q1 (b)
print("")
print("Q1 (b)(i) PMF of Recovered Patients (Age wise)")
plotting(r,"Age vs No. of cases for Recovered patients",rm,rv)
print("Q1 (b)(ii) PMF of Dead Patients (Age wise)")
plotting(d,"Age vs No. of cases for Dead patients",dm,dv)
print("Therefore it can be said that the chances of death due to Covid-19 increases with age and people with less age have more chances to be recovered")

# Q1 (c)
print("")
print("Q1 (c)(i) PMF of Male Patients (Age wise)")
plotting(m,"Age vs No. of cases for Male patients",mm,mv)
print("Q1 (c)(ii) PMF of Female Patients (Age wise)")
plotting(f,"Age vs No. of cases for Female patients",fm,fv)
print("With expected age of male and female patients almost similar but variances different, we can conclude that in the case of males, covid is spread out to many age group in enough amounts, while for females, covid is more concentrated at women aged 38-39")

# Q2 (a)
d1=pd.read_excel("Incubation_IncludingWR.xlsx")
x1=d1['Incubation Period'].values

ip1={}
inc1=0


for i in x1:
    inc1+=1
    if i in ip1:
        ip1[i]+=1
    else:
        ip1[i]=1

ip1=sortdict(ip1,inc1)
ip1m=expect(ip1)
ip1v=varianc(ip1,ip1m)

print("")
print("Q2 (a) PMF of the all patients (including Wuhan Residents)")
print("Note:")
print("1. Only Travel to Wuhan, Contact with case, Contact with Wuhan resident and Lives-works-studies in Wuhan cases are considered for plotting this graph and calculation of the Incubation Period" )
print("2. For Lives-works-studies in Wuhan, those whose ExposurL was not given, is assumed as 01-12-2019 i.e. the reporting date of first covid patient")
plotting(ip1,"Incubation Period Graph for all the patients",ip1m,ip1v)

# Q2 (b)
d2=pd.read_excel("Incubation_ExcludingWR.xlsx")
x2=d2['Incubation Period'].values

ip2={}
inc2=0


for i in x2:
    inc2+=1
    if i in ip2:
        ip2[i]+=1
    else:
        ip2[i]=1

ip2=sortdict(ip2,inc2)
ip2m=expect(ip2)
ip2v=varianc(ip2,ip2m)

print("")
print("Q2 (b) PMF of the patients excluding Wuhan Residents")
print("Note: Only Travel to Wuhan, Contact with case, Contact with Wuhan residens are considered for plotting this graph and calculation of the Incubation Period" )
plotting(ip2,"Incubation Period Graph for patients Excluding Wuhan Residents",ip2m,ip2v)
print("There is a large difference between the Incubation Period in both cases which shows that Wuhan residents were exposed to the virus a long time before and thus it could have been controlled way back if the matter was dealt seriously")

# Q2 (c)
# (Part 1)
d3=pd.read_excel("Onset_Hospitalisation_Death.xlsx")
x3=d3['H-O'].values
x4=d3['X-O'].values
x5=d3['X-H'].values

ip3={}
ip4={}
ip5={}
inc3=0
inc4=0
inc5=0

for i in x3:
    inc3+=1
    if i in ip3:
        ip3[i]+=1
    else:
        ip3[i]=1
        
for i in x4:
    inc4+=1
    if i in ip4:
        ip4[i]+=1
    else:
        ip4[i]=1
        
for i in x5:
    inc5+=1
    if i in ip5:
        ip5[i]+=1
    else:
        ip5[i]=1
        
ip3=sortdict(ip3,inc3)
ip3m=expect(ip3)
ip3v=varianc(ip3,ip3m)

print("")
print("Q2 (c) (i) PMF of the onset to hospitalization (O-H) of dead ptients")
plotting(ip3,"PMF of the onset to hospitalization (O-H) of dead patients",ip3m,ip3v)

ip4=sortdict(ip4,inc4)
ip4m=expect(ip4)
ip4v=varianc(ip4,ip4m)

print("")
print("Q2 (c) (ii) PMF of the onset to death (O-X) of the patients")
plotting(ip4,"PMF of the onset to death (O-X) of the patients",ip4m,ip4v)

ip5=sortdict(ip5,inc5)
ip5m=expect(ip5)
ip5v=varianc(ip5,ip5m)

print("")
print("Q2 (c) (iii) PMF of the hospitalization to death (H-X) of the patients")
plotting(ip5,"PMF of the hospitalization to death (H-X) of the Patients",ip5m,ip5v)
print("The three graphs are quite similar and it can be said that, more the days it took for the patients to visit the hospital, their chance of surviving became less")

# (Part 2)
d6=pd.read_excel("H-O_All_Patients.xlsx")
x6=d6['H-O'].values

ip6={}
inc6=0


for i in x6:
    inc6+=1
    if i in ip6:
        ip6[i]+=1
    else:
        ip6[i]=1

ip6=sortdict(ip6,inc6)
ip6m=expect(ip6)
ip6v=varianc(ip6,ip6m)

print("")
print("Q2 (c) (iv) PMF of the onset to hospitalization (O-H) of the survived patients")
print("Note: All the cases of survived patients have been included in this plot")
plotting(ip6,"PMF of the onset to hospitalization (O-H) of the survived patients",ip6m,ip6v)
print("It is clear by the plot that the sooner the sooner the patient was reported to the hospital, more became his chances of surviving")