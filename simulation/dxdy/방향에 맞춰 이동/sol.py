n=int(input())
dx,dy=[1,0,-1,0],[0,-1,0,1]

nx,ny=0,0
for _ in range(n):
    command,k=input().split()
    k=int(k)

    if command=='E':
        move=0
    elif command=='S':
        move=1
    elif command=='W':
        move=2
    elif command=='N':
        move=3
    nx+=dx[move]*k
    ny+=dy[move]*k

print(nx,ny)

#O(n)