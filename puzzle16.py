import time

#  Movimentos possiveis para 16 pecas - mod
def movimentos(v,x):
    mov_possiveis=[]
    if x%4-1 in range (0,4):
        aux = v[:] 
        aux[x] = v[x-1]
        aux[x-1] = 16
        mov_possiveis.append(aux)
    
    if x%4+1 in range (0,4):
        aux = v[:]
        aux[x]=v[x+1]
        aux[x+1] = 16
        mov_possiveis.append(aux)
    
    if x+4 in range (0,16):
        aux = v[:]
        aux[x] = v[x+4]
        aux[x+4] = 16
        mov_possiveis.append(aux)
        
    if x-4 in range (0,16):
        aux = v[:]
        aux[x] = v[x-4]
        aux[x-4] = 16
        mov_possiveis.append(aux)
    return mov_possiveis

# Heuristica da distancia de Manhatan

def distancia(a):
    h = 0
    d = 0
    while(d<16):
        y = abs(a[d] - 1 - d)
        h = h +y//4 + y%4
        d = d + 1
    return h

# duas listas, uma com nos x e outra com nos pais e outras informacoes 
# a unica diferenca real sao as dimencoes de cada lista
# o objetivo aqui eh o pai do pai (o pai de um no sera uma no) montando assim um caminho de no em no  

def getCaminho(x, y):
    index = len(x) - 1
    caminho = []
    while(index > 0):
        filho = y[index][0] #adiciona filho no caminho
        caminho.append(filho)
        pai = y[index][2]
        index = x.index(pai)
    caminho.reverse()
    return caminho
    
#imprimir caminho

def desCaminho(x): 
    for i in x:
        print("------------------")
        print(i[0:4])        
        print(i[4:8])        
        print(i[8:12])       
        print(i[12:16])
        print("------------------")
        
def indexNoFront(v, i):
    aux = 0
    for a in v:
        if a[0] is i:
            return aux
        aux = aux+1

def nodoSon(v, i):
    for a in v:
        if a[0] is i:
            return True
    return False
        
def algoritmoAEstrela(v):
    inicio = time.time() #para calculo de tempo
    h = distancia(v)
    g = 0
    aux = v[:]
    visitados = [v]
    visitadosComp = [[v, h, [], 0]]
    front = [[v, h, [], 0]]
    i=0

    print("Aguarde...")
    while(h>0):
        for vet in movimentos(aux, aux.index(16)):
            if not(vet in visitados):
                f = distancia(vet) + g
                front.append([vet, f, aux, g])
            elif nodoSon(front, vet):
                index = indexNoFront(front, vet)
                custo = front[index][3]
                if custo > g:
                    f = distancia(vet) + g
                    del front[index]
                    front.append([vet, f, aux, g])
                    
                    
        front.sort(key=lambda x: x[1])
        aux = front[0][0]
        visitados.append(aux)
        h = distancia(aux)
        g = front[0][3] + 1
        visitadosComp.append(front[0])
        del front[0]
        i=i+1
        
    fim = time.time()
    tempo = fim - inicio #tempo calculado

    caminho = getCaminho(visitados, visitadosComp)
    desCaminho(caminho)
    print("Resolvido em ", len(caminho)," passos.")
    print("Tempo de solucao: ", tempo)
    print(i," foram Nos expandidos.")

caso1 = [2,6,3,4,1,10,7,8,5,11,16,12,9,13,14,15]
#caso2 = [6,2,3,4,1,10,7,8,5,11,16,12,9,13,14,15] #alguns casos podem demorar bastante
algoritmoAEstrela(caso1)       