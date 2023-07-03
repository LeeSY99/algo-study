n,m=map(int,input().split())
answer=[]
dr,dc=[0,1,0,-1],[1,0,-1,0]
for _ in range(n):
    answer.append(list([0]*m))

def in_range(nr,nc):
    return 0<=nr<n and 0<=nc<m

r,c=0,0
dir=0
answer[r][c]=1
for i in range(2,n*m+1):
    nr=r+dr[dir]
    nc=c+dc[dir]
    if not in_range(nr,nc) or answer[nr][nc]!=0:
        dir=(dir+1)%4
    r,c=r+dr[dir], c+dc[dir]
    answer[r][c]=i

for a in answer:
    print(*a)
