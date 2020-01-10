import json

def change_test():
    f = open("aux.json","r")
    data = json.loads(f.read())
    data["address"][0]["phone123"] = data["address"][0].pop("phone")
    print(data["address"][0])
    f2 = open("aux.json","w")
    json.dump(data,f,indent=4)

# Função que encontra o objeto cidade com o id passado
def find_city(id):
    f = open("../oldJson/city.json","rb")
    citys = json.loads(f.read())
    i = 0
    while(i < 600):
        #print(citys["city"][i]["city_id"])
        if(citys["city"][i]["city_id"] == id):
            return citys["city"][i]
        i+=1
    return 

# Função que encontra o nome do paíscom o id passado
def find_country(id):
    f= open("../oldJson/country.json","rb")
    countries = json.loads(f.read())
    i = 0
    countr = countries["country"]
    while(i < 109):
        if(countr[i]["country_id"] == id):
            return countr[i]["country"]
        i+=1
    return

#Função que processa os endereços 
def processAddresses():
    f = open("../oldJson/addresses.json","rb")
    addresses = json.loads(f.read()) 
    i = 0
    while(i < 603):
        if(addresses["address"][i]):
            address = addresses["address"][i]
            # FIND CITY AND COUNTRY
            city = find_city(address["city_id"])
                #print(city)
            city_name = city["city"]
            country = find_country(city["country_id"])
                #print(country)
            # CHANGE FIELDS AND VALUES
            address.pop("city_id")
            address["city"] = city_name 
            address["country"] = country
            address.pop("address2")
            address.pop("last_update")
            address.pop("phone")
        i+=1
    
    new = open("../newJson/addresses.json","w")
    json.dump(addresses,new,indent=4)


processAddresses()