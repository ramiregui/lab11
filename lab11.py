#Guilherme Ramirez RA217295
l = input()
ints = [int(i) for i in l.split()]
m=ints[0]#matriz "real" dos zumbis
n=ints[1]
dias=input()
linha=ints[0]+2
coluna=ints[1]+2
mat = [ [ [] for j in range(coluna) ] for i in range(linha) ]#cria a matriz aumentada com zeros nas bordas
for j in range(coluna):
    mat[0][j]=0
    mat[linha-1][j]=0
for i in range(linha):
    mat[i][0]=0
    mat[i][coluna-1]=0
for x in range(1,m+1):
    entrada=input()
    lzumbis = [int(i) for i in entrada.split()]
    for y in range(1,n+1):
        u=y-1
        mat[x][y]=lzumbis[u]
print("iteracao 0")
lll=str()
for x in range(1,m+1):
    for y in range(1,n+1):
        lll=lll+str(mat[x][y])
    print(lll)
    lll=str()
#já conseguimos colocar os dados em uma matriz
#    Se X for humano e possuir pelo menos um vizinho zumbi, então X é infectado e se torna um zumbi no dia seguinte;
#    Se X for zumbi e possuir dois ou mais vizinhos humanos, ele é caçado e morto pelos humanos;
#    Se X for zumbi e não possuir nenhum vizinho humano, ele morre de fome e fica vazio no dia seguinte;
#    Se X estiver vazio e possuir exatamente dois vizinhos humanos, independente dos demais vizinhos serem zumbis ou vazio, então um humano nasce em X no dia seguinte.
#    Se nenhuma das alternativas anteriores for verdade, então X permanece como está.
a=1
while a<=int(dias):
    print("iteração "+str(a))
    mataux= [ [ [] for j in range(coluna) ] for i in range(linha) ]#cria a matriz aumentada com zeros nas bordas
    for j in range(coluna):
        mataux[0][j]=0
        mataux[linha-1][j]=0
    for i in range(linha):
        mataux[i][0]=0
        mataux[i][coluna-1]=0
    for x in range(1,m+1):
        for y in range(1,n+1):
            q=mat[x][y]
            mataux[x][y]=q
    #essa parte de cima "copia" a matriz para uma auxiliar
    for x in range(1,m+1):
        for y in range(1,n+1):
            nz=0
            nh=0
            if mat[x][y]==2:#zumbi
                if mat[x-1][y-1]==1:
                    nh=nh+1
                if mat[x-1][y]==1:
                    nh=nh+1
                if mat[x-1][y+1]==1:
                    nh=nh+1
                if mat[x][y-1]==1:
                    nh=nh+1
                if mat[x][y+1]==1:
                    nh=nh+1
                if mat[x+1][y-1]==1:
                    nh=nh+1
                if mat[x+1][y]==1:
                    nh=nh+1
                if mat[x+1][y+1]==1:
                    nh=nh+1
                if nh>=2:
                    mataux[x][y]=0
                if nh==0:#a celula fica vazia
                    mataux[x][y]=0
            elif mat[x][y]==1:#humano
                if mat[x-1][y-1]==2:
                    nz=nz+1
                if mat[x-1][y]==2:
                    nz=nz+1
                if mat[x-1][y+1]==2:
                    nz=nz+1
                if mat[x][y-1]==2:
                    nz=nz+1
                if mat[x][y+1]==2:
                    nz=nz+1
                if mat[x+1][y-1]==2:
                    nz=nz+1
                if mat[x+1][y]==2:
                    nz=nz+1
                if mat[x+1][y+1]==2:
                    nz=nz+1
                if nz>=1:
                    mataux[x][y]=2
            elif mat[x][y]==0:#vazio
                if mat[x-1][y-1]==1:
                    nh=nh+1
                if mat[x-1][y]==1:
                    nh=nh+1
                if mat[x-1][y+1]==1:
                    nh=nh+1
                if mat[x][y-1]==1:
                    nh=nh+1
                if mat[x][y+1]==1:
                    nh=nh+1
                if mat[x+1][y-1]==1:
                    nh=nh+1
                if mat[x+1][y]==1:
                    nh=nh+1
                if mat[x+1][y+1]==1:
                    nh=nh+1
                if nh==2:
                    mataux[x][y]=1
                elif nh!=2:
                    mataux[x][y]=0
    lll=str()
    for x in range(1,m+1):
        for y in range(1,n+1):
            lll=lll+str(mat[x][y])
        print(lll)
        lll=str()
    a=a+1
    mat=mataux
