n=int(input('Enter number:'))
temp=n
rev=0
while(n>0):
n=n//10
if(temp==rev):
 print('The number is palindrome')
 else:
  print('The number is not palindrome')
