def a(n,b):
global r
if(len(b)==0):
return false
while(b[0]>n):
b.remove(b[0]):
if(len(b)==0):
return false
if(b[0]==n):
r.append(b[0])
return true
if(len(b)==1):
return false
