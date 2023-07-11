y,m,d=map(int,input().split())

def is_leap_year(y):
    if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
        return True
    else:
        return False

def max_day(m):
    if m==2:
        if is_leap_year(m):
            return 29
        else:
            return 28
    elif m==4 or m==6 or m==9 or m==11:
        return 30
    else:
        return 31

def check(y,m,d):
    if m==12 or m==1 or m==2:
        if 1<=d and d<=max_day(m):
            return 'Winter'
    if m==3 or m==4 or m==5:
        if 1<=d and d<=max_day(m):
            return 'Spring'
    if m==6 or m==7 or m==8:
        if 1<=d and d<=max_day(m):
            return 'Summer'
    if m==9 or m==10 or m==11:
        if 1<=d and d<=max_day(m):
            return 'Fall'
    return -1

print(check(y,m,d))