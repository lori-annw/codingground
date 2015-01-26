import math

with open('randTSP/10/instance_1.txt') as f:
    content = f.readlines()
    
#we assume at lease one city
dict = {}
numCities = int(content[0]);
for x in range(1,numCities+1):
    contentlst = content[x].split(" ")
    city = contentlst[0]
    x = int(contentlst[1])
    y = int(contentlst[2])
    dict[city] = (x,y)

print (dict)

def g (city1, city2):
    x1 = city1[0]
    x2 = city2[0]
    y1 = city1[1]
    y2 = city2[1]
    dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist
    

#define loop here 


print ( g (dict['A'], dict['D']) )