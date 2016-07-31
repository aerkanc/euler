
a=0; c=0; max=0;
while max<=500:
   c+=1; a+=c; d=0; b=0; x=1
   while a/x != b:
      if a%x==0:
         if x*x==a:
            d+=1
            break
         b=x
         d+=2
      x+=1
   if d>max:
      max=d
      print(d,a)