#exercise 6b
a = int(input("Enter a start value:"))
b = int(input("Enter a stop value:"))
for a in range(a,b):
    if  (a%7)==0  and (a%5)!=0:
        print(a,end= "\n")
    else:
          if(a%5)==0:
              print("nothing")
        
