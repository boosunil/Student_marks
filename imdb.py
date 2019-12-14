import json
data=open('imdb_movies1.json','r')
p=json.load(data)
#print(p)

#Top 10 least watched movies according to imdb_score
l = sorted(p, key=lambda x: x['imdb_score'])
# print(l)
print("Top 10 least watched movies according to imdb_score:")
for i, x in enumerate(l, start=1):
    if i <= 10:
        print(i,'.',x['name'])


#Top 10 most watched movies according to imdb_score
print()
l = sorted(p, key=lambda x: x['imdb_score'],reverse=True)
# print(l)
print("Top 10 most watched movies according to imdb_score:")
for i, x in enumerate(l, start=1):
    if i <= 10:
        print(i,'.',x['name'])

#Director with most number of movies
print()
n = max(l,key=lambda x:len(x['genre']))
l1 = len(n['genre'])
print("Director with most number of movies:")
for x in l:
    if len(x['genre']) == l1:
        print(x['director'],"with",len(x['genre']),"movie genres")


#Who is the best director in the first hundred movies
print()
l2 = []
for i, x in enumerate(p,start=1):
    if i<=100:
        l2.append(x)
m = max(l2, key=lambda x:x['99popularity'])
a = m['99popularity']
for x in l2:
    if x['99popularity'] == a:
        print("Best director in top hundred movies:",x['director'],x['99popularity'])

#Query 2. What is the popular genere watched by most of the audiance?
print()
l3 = []
for i in p:
    l3.append(i['genre'])
l4 = []
for x in range(len(l3)):
    for y in range(len(l3[x])):
        l4.append(l3[x][y])
d = {}
for z in l4:
    if z not in d:
        d[z] = 1
    else:
        d[z]+=1
print("Most repeated genre is:")
l3 = max(d.items(),key=lambda x:x[1])
print(l3)
#Query 2. What is the popular genere watched by most of the audiance?
print()
l5 = []
for i,x in enumerate(p):
    l5.append(x)
k = max(l5,key=lambda x:x['99popularity'])
max_by_pub = k['99popularity']
for x in l5:
    if x['99popularity'] == max_by_pub:
        print("The most watched movies by public is:",x['name'],"with :",x['99popularity'],"%")
