import json

def find_actor(id):
    f = open("../oldJson/atores.json","r")
    actores = json.loads(f.read())
    actor = actores["actor"]
    i = 0
    if(id == "110"):
        end = " (2)"
    else:
        end = ""
    while(i < 201):
        if(actor[i]["actor"] == id):
            actor[i].pop("last_update")
            actor[i].pop("actor")
            fn = actor[i]["first_name"]
            ln = actor[i]["last_name"]
            actor[i]["name"] = fn + " " + ln + end
            actor[i].pop("first_name")
            actor[i].pop("last_name")
            #return (actor[i])
            return actor[i]["name"]
        i+=1
    return

def find_actores_filme(idFilme):
    f = open("../oldJson/film_actor.json","r")
    data = json.loads(f.read())
    data = data["film_actor"]
    i = 0
    j = 0
    actors = []
    while(i < 5462):
        #print("welelele")
        if(data[i]["film_id"] == idFilme):
            actor = find_actor(data[i]["actor_id"])
            actors.insert(j,actor)
            j+=1
        i+=1
    return actors


# Função que encontra o objeto cidade com o id passado
def find_language(id):
    f = open("../oldJson/language.json","rb")
    languages = json.loads(f.read())
    i = 0
    while(i < 6):
        if(languages["language"][i]["language_id"] == id):
            return languages["language"][i]["name"]
        i+=1
    return 

def find_category(id):
    f = open("../oldJson/category.json","rb")
    cats = json.loads(f.read())
    i = 0
    while(i < 16):
        if(cats["category"][i]["category_id"] == id):
            return cats["category"][i]["name"]
        i+=1
    return 


# Função que encontra o nome do paíscom o id passado
def find_film_category(id):
    f= open("../oldJson/film_category.json","rb")
    films = json.loads(f.read())
    i = 0
    film = films["film_category"]
    while(i < 1000):
        if(film[i]["film_id"] == id):
            cat = find_category(film[i]["category_id"])
            return cat
        i+=1
    return


#Função que processa os endereços 
def processFilms():
    f = open("../oldJson/film.json","rb")
    films = json.loads(f.read()) 
    i = 0
    while(i < 1000):
        if(films["film"][i]):
            film = films["film"][i]
            # FIND LANGUAGE
            language = find_language(film["language_id"])
                #print(language)
            # FIND CATEGORY
            category = find_film_category(film["film_id"])
                #print(category)
            actors = find_actores_filme(film["film_id"])
            #print(actors)
            # CHANGE FIELDS AND VALUES
            film.pop("language_id")
            film["language"] = language
            film["category"] = category
            film["actors"] = actors
            film.pop("original_language_id")
            film["film_id"] = int(film["film_id"])

        i+=1

    new = open("../newJson/film.json","w")
    json.dump(films,new,indent=3)


processFilms()