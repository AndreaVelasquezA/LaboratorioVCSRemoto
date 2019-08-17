a=int(input("digite el numero a:"))
b=int(input("digite el numero b:"))
c=int(input("digite el numero c:"))
import math
d=math.sqrt((b*b)-4*a*c)
x1=(-b+math.sqrt(d))/2*a
x2=((-b)/2*a)

if d<0:
  print("no existe solucion")
else:
    if d==0:
       print("solucion:",x2)
    else:
       if d>0:
        print("solucion:",x1)
     
     
   

