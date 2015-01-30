import math

with open('randTSP/10/instance_1.txt') as f:
    content = f.readlines()
    
#we assume at lease one city
dictOfCities = {}
numCities = int(content[0]);
for x in range(1,numCities+1):
    contentlst = content[x].split(" ")
    city = contentlst[0]
    x = int(contentlst[1])
    y = int(contentlst[2])
    dictOfCities[city] = (x,y)

print (dictOfCities)

def g (city1, city2):
    distance(city1,city2)

def distance (city1,city2):
    x1 = city1[0]
    x2 = city2[0]
    y1 = city1[1]
    y2 = city2[1]
    dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist
    
    
distances = {}
for i in dictOfCities.keys():
    for j in dictOfCities.keys():
        
        lst[j] = distance()
    distances.append(lst)
    

#define loop here 


print ( g (dictOfCities['A'], dictOfCities['D']) )
