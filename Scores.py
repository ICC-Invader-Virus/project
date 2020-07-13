def highscore(m):
    pivote=m[0]
    menores=[]
    mayores=[]
    máximo=0
    for i in range(0,len(m)):
        if m[i]<pivote:
            menores.append(m[i])
        else:
            mayores.append(m[i])
    máximo+=max(mayores)
    b=str(máximo)
    p=n+":"+b
    a=open("el nombre de cualquier archivo","a")
    a.write("\n")
    a.write(p)
    a.close()
    a=open("el nombre de cualquier archivo","r")
    for i in a:
        print(i,end="")
    a.close()

def singlescore(m):
    if len(m)<2:
        b=str(m[0])
    p=n+":"+b
    a=open("el nombre de cualquier archivo","a")
    a.write("\n")
    a.write(p)
    a.close()
    a=open("el nombre de cualquier archivo","r")
    for i in a:
        print(i,end="")
    a.close()
#Lo de abajo es una comprobación si el código funciona o no
n=input("Nombre del jugador: ")
m=[900,40]
if len(m)<2:
    singlescore(m)
else:
    highscore(m)
