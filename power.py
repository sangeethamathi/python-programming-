x=2,3
if(exp==1):
 return(2)
if(exp!=1):
 return(base*power(base,exp-1))
 base=int(input('Enter the base:'))
 exp=int(input('Enter exponential value:'))
 print('Result:',power(base,exp))
