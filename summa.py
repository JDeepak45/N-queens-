
k=[]
n=int(input())
def prin(k):
    for i in range(n):
        for j in range(n):
            print(k[i][j],end=' ')
        print()

def safe(k,i,j):
    for m in range(j):
        if k[i][m]==1:
            return False
    for m,q in zip(range(i,-1,-1),range(j,-1,-1)):
        if k[m][q]==1:
            return False
    for m,q in zip(range(i,n,-1),range(j,-1,-1)):
        if k[m][q]==1:
            return False
    return True
    

def s(k,col):
    if col>=n:
        return True
    else:
        for j in range(n):
            if safe(k,j,col):
                k[j][col]=1
                if s(k,col+1):
                    return True
                k[j][col]=0
    return False
                


for i in range(n):
    l=[]
    for j in range(n):
        l.append(0)
    k.append(l)
s(k,0)
prin(k)