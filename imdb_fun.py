import json
data=open('imdb_movies1.json','r')
p=json.load(data)

#Top 10 movies based on imdb_score
def top_ten_movies(*args,**kwargs):
    print()
    print("Top 10 movie with top imdb_score is:")
    l = sorted(p,key=lambda x:x['imdb_score'])
    for i,x in enumerate(l,start=1):
        if i<=10:
            print(i,'.',x['name'])

# 10 movies with least imdb_score
def least_ten_movies(*args,**kwargs):
    print()
    print("Least imdb_score is:")
    l = sorted(p, key=lambda x: x['imdb_score'],reverse=True)
    for i, x in enumerate(l, start=1):
        if i <= 10:
            print(i, '.',x['name'])

#Top Director based on Genre
def top_director(*args,**kwargs):
    print()
    n = max(l, key=lambda x: len(x['genre']))
    l1 = len(n['genre'])
    print("Director with most number of movies:")
    for x in l:
        if len(x['genre']) == l1:
            print(x['director'], "with", len(x['genre']), "movie genres")

#Best Director in top 100 movies
def best_dir_in_100(*args,**kwargs):
    print()
    l2=[]
    for i,x in enumerate(l,start=1):
        if i<=100:
            l2.append(x)
    a = max(l2,key=lambda x:x['99popularity'])
    m = a['99popularity']
    for x in l2:
        if x['99popularity'] == m:
            print("Best director with maximum number of movies:",x['director'], x['99popularity'])


top_ten_movies(p)
least_ten_movies(p)
top_director(p)
best_dir_in_100(p)