from pyeda.inter import *
from graphviz import Source
class Parse():
   def __init__(self):
        buf=''
        self.var=''
        self.variable=[]
        self.flag=True
        self.sdnf=[]
        self.len=[]
        self.f = open('truth_table.txt', 'r')
        for line in self.f:
            for i in range(len(line)):
                if line[i-1]=="\\":
                    while(line[i]!=" "):
                        self.var+=line[i]
                        if (i+1)<len(line):
                            i+=1
                        else:
                            self.var=self.var[0:len(self.var)-1]
                            line+=' '
                            i+=1
                    self.variable.append(self.var)
                    self.var=''

        self.f = open('truth_table.txt', 'r')
        for line in self.f:
            for i in range(len(line)):
                if line[i]=="|":
                    buf=line[i::]
            for i in range(len(buf)):
                if buf[i]=="'":
                    if self.flag==True:
                        self.len.append(buf[i-1])
                        self.flag=False

        for i in range(len(self.len)):
            for j in range(int(self.len[len(self.len)-1-i])):
                self.sdnf.append(self.variable[len(self.variable)-1-i]+str(j)+'=')


        print(self.sdnf)
        print(self.variable)


class dnf():
    def __init__(self, variables,sdnf):
        self.f = open('truth_table.txt', 'r')
        self.variables=variables
        self.formul=''
        self.counter=-1
        self.counter_two=0
        self.sdnf=sdnf
        self.buf=sdnf.copy()
        i=0
        for line in self.f :
            i=0
            count=0
            flag=True
            self.formul=''
            self.counter=0
            self.counter_two = 0
            while (i<len(line)):
                if line[i]=="|":
                    flag=False
                    count=i
                if flag==True:
                    if line[i]=="'":
                        self.len=line[i-1]
                        z=0
                        while(z<int(self.len)):

                            if line[i+1+z]=='0':
                                if len(self.formul)>1:
                                    self.formul+='&~'+self.variables[self.counter]+str(z)
                                else: self.formul+='!'+self.variables[self.counter]+str(z)
                            if line[i+1+z]=='1':
                                if len(self.formul) > 1:
                                    self.formul+='&'+self.variables[self.counter]+str(z)
                                else:
                                    self.formul += '' + self.variables[self.counter] + str(z)
                            z+=1
                        self.counter += 1

                i+=1
            buf=line[count+1::]

            i=0
            while (i < len(buf)):
                if buf[i:i+1]!="\\n":
                    if buf[i]=="'":
                        self.len=buf[i-1]
                        for j in range(int(self.len)):
                            if buf[i+1+j]=='1':
                                print(self.buf)
                                if len(self.sdnf[self.counter_two+j])>len(self.buf[self.counter_two+j]):
                                    self.sdnf[self.counter_two+j]+='|('+self.formul+')'
                                else: self.sdnf[self.counter_two+j]+='('+self.formul+')'
                        self.counter_two+=int(self.len)
                i+=1

a=Parse()
b=dnf(a.variable,a.sdnf)
print(b.sdnf)
for i in range(len(b.sdnf[0])):
    if b.sdnf[0][i]=="=":
        buf=b.sdnf[0][i+1::]
s=expr(buf)
s=expr2bdd(s)
gv=Source(s.to_dot())
gv.render('out.pdf',view=True)








