a = int(input("What type of equations is this ? Enter 1 for linear equation, 2 for quadratic equation, 3 for cubic equation, 4 for bi-quadratic equation and so on : "))
c=[];f={}
for x in range(0,a+1):
    b = int(input("Enter coefficient from lower to higher power : "))
    c.append(b)
print(c)
d=len(c)
print("\nNumber of coefficients : ",d,"\n")
print("Equation is : ")
for y in range(d):
     if y!=(d-1):
        print(c[y],"x^",y,sep="",end = " + ")
     else:
         print(c[y],"x^",y,sep="",end = " ")
print("\n")         
for z in range(-d-5,d+5):       
    def r(z):
        sum = 0
   #for z in range(d):
        for q in range(d):
            e = (z**q)*c[q]
            sum = sum + e
        #print("\n",sum)
        #break
        return sum
    r(z)
    f.update([(z,r(z))])
print(f)
for a in f:
    if (f[a]<0 and f[a+1]>0):
        ''' or (f[a]>0 and f[a+1]<0)'''
        AA = a
        BB = a+1
        fa = f[a]
        fb = f[a+1]
        break
print("\nIteration 1 : \n")
print("\na = ",AA,"b = ",BB)
print("f(a) = ",fa,"f(b) = ",fb)
summ = 0
for x in range(10):
    cc = round(((AA*fb) - (BB*fa))/(fb - fa),3)
    print("C = ",cc)
    for z in range(d):
        q = round(((cc**z)*(c[z])),3)
        summ = summ + q
    print("f(c) = ",round(summ,3),"\n")
    print("\nIteration : ",x+2,"\n")
    if summ > 0 :
        BB = cc
        print("a = ",AA)
        print("b = ",BB)
        fb = round(summ,3)
        print("f(a) = ",fa)
        print("f(b) = ",fb,"\n")
    if summ < 0 : 
        AA = cc
        print("a = ",AA)
        print("b = ",BB)
        fa = round(summ,3)
        print("f(a) = ",fa)
        print("f(b) = ",fb,"\n")
    summ = 0