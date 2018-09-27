res*=((a*a)%n):
res%=n:
if(b%n==1):
res&=a;
res*=n;
return res;
