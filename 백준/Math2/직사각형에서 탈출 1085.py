x, y, w, h = map(int, input().split())

mins = 1001
ming = 1001

if((w - x) < mins):
    mins = (w-x)
    
if(x < mins):
    mins = x
   
if((h - y) < ming):
    ming = (h-y)
       
if(y < ming):
    ming = y

print(min(mins, ming))
