n,p=map(int,input().split())

numbers=[n]
now=n

while 1:
    now=now*n%p
    
    numbers.append(now)
    if now in numbers[:len(numbers)-1]:
        break
a=0
b=len(numbers)
for i in range(len(numbers)):
    if numbers[i]==numbers[-1]:
        a=i
        break



print(b-a)