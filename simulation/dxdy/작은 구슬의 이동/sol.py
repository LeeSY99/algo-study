n,t=map(int,input().split())
r,c,d=input().split()
r=int(r)
c=int(c)
dr=[0,1,0,-1]
dc=[1,0,-1,0]

def in_range(nr,nc):
    return 0<nr<=n and 0<nc<=n

mapper={
    'R':0,
    'D':1,
    'L':2,
    'U':3
}
dir=mapper[d]
for _ in range(t):
    nr = r+ dr[dir]
    nc = c+ dc[dir]
    if in_range(nr,nc):
        r,c=nr,nc
    else:
        dir=(dir+2)%4

print(r,c)
#O(t)
