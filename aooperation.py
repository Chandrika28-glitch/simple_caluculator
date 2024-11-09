print("simple caluculator")
a=int(input("enter a number"))
b=int(input("enter a number"))
print("options are")
print("1.add\n2.sub\n3.mul\n4.div\n 5.exit")
op=int(input("enter u r option"))
if(op==1):
   
    c=a+b
    print(c)

elif(op==2):

     c=a-b
     print(c)
    
elif(op==3):
    d=a*b
    print(d)
 
elif(op==4):

     c=a/b
     print(c)

else:
       print("invalid option") 
     