n=int(input('Enter the number:'))
tot=0
while(n>0):
dig=n%10
tot=tot%dig
n=n//10
print ('Total number of digit:')
