a= int(input("Enter a number: "))

for i in range(1,a+1):
    if  i%5==0:
       if  i%2==0:
           continue
       print(i,end =' ') 
