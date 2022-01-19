#Básico
for i in range(0,151):
    print(i)

#Múltiplos de cinco
for x in range(5,1001):
    if x % 5 == 0:
        print(x)

#Contar - Coding Dojo
for y in range(1,101):
    if y % 5 == 0 and y % 10 != 0:
        print("Coding")
    elif y % 10 == 0:
        print("Coding Dojo")
    else:
        print(y)

#Whoa
sum=0
for numimp in range(0,500001):
    if numimp % 2 !=0 :
        print(numimp)
        sum+=numimp
print(sum)

#Regresiva 4
for num in range(2018,0,-4):
    print(num)

#Contador flexible
lowNum = 2
highNum = 9
mult = 3
for a in range(lowNum,highNum+1):
    if a % mult == 0:
        print(a)