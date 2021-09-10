#checking greater number
a=int(input("Enter first number a:"))
b=int(input("Enter second number b:"))
c=int(input("Enter third number c:"))
if(a>b):
  if(a>c):
    print( a,"is greatest number")
  else:
    print(b,"is greatest number")
else:
  if(b>c):
    print(b,"is greatest")
  else:
    print(c,"is greatest")
