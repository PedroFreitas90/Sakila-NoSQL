import json
from datetime import datetime


#----------------------- PAYMENT INFORMATION ------------------#
def find_payment(rental_id):
    f = open("../oldJson/payment.json","rb")
    payments = json.loads(f.read())
    i = 0
    payment = payments["payment"]
    size = len(payment)
    while(i < size):
        if(payment[i]["rental_id"] == rental_id):
            return float(payment[i]["amount"])
        i+=1
    return
#----------------------- PAYMENT INFORMATION ------------------#


#----------------------- STAFF INFORMATION --------------------#
def find_location(address_id):
    f = open("../newJson/addresses.json","rb")
    addresses = json.loads(f.read())
    i = 0 #contador para percorrer staff
    address = addresses["address"]
    size = len(address)
    while(i < size):
        if(address[i]["address_id"] == address_id):
            add = address[i]["address"]
            city = address[i]["city"]
            district = address[i]["district"]
            country = address[i]["country"]
            return add,city,district,country
        i+=1
    return    

def find_store(store_id):
    f = open("../oldJson/store.json","rb")
    stores = json.loads(f.read())
    i = 0 #contador para percorrer staff
    store = stores["store"]
    size = len(store)
    while(i < size):
        if(store[i]["store_id"] == store_id):
            return find_location(store[i]["address_id"])
        i+=1
    return ("","","","")

def find_staff(staff_id):
    f = open("../oldJson/staff.json","rb")
    staffs = json.loads(f.read())
    i = 0 #contador para percorrer staff
    staff = staffs["staff"]
    size = len(staff)
    while(i < size):
        if(staff[i]["staff_id"] == staff_id):
            name = staff[i]["first_name"] + " " + staff[i]["last_name"]
            mail = staff[i]["email"]
            store_id = staff[i]["store_id"]
            staff[i].pop("email")
            staff[i].pop("store_id")
            staff[i].pop("password")
            staff[i].pop("username")
            staff[i].pop("active")
            staff[i].pop("address_id")
            staff[i].pop("first_name")
            staff[i].pop("last_name")
            address,city,district,country = find_store(store_id)
            staff[i]["name"] = name
            staff[i]["email"] = mail
            staff[i]["store_id"] = store_id
            staff[i]["store_address"] = address
            staff[i]["store_city"] = city
            staff[i]["store_district"] = district
            staff[i]["store_country"] = country
            return staff[i]
        i+=1
    return
#----------------------- STAFF INFORMATION --------------------#


#----------------------- FILM INFORMATION ---------------------#
def find_film(film_id):
    f = open("../newJson/film.json","rb")
    films = json.loads(f.read())
    i = 0 #contador para percorrer staff
    film = films["film"]
    size = len(film)
    while(i < size):
        if(film[i]["film_id"] == film_id):
            #print(film[i])
            film[i].pop("release_year")
            film[i].pop("rental_duration")
            film[i].pop("rental_rate")
            film[i].pop("length")
            film[i].pop("replacement_cost")
            film[i].pop("rating")
            film[i].pop("last_update")
            return film[i]
        i+=1
    return

def find_inventory(inventory_id):
    f = open("../oldJson/inventory.json","rb")
    invs = json.loads(f.read())
    i = 0 #contador para percorrer staff
    inventory = invs["inventory"]
    size = len(inventory)
    while(i < size):
        if(inventory[i]["inventory_id"] == inventory_id):
            film = find_film(int(inventory[i]["film_id"]))
            return film
        i+=1
    return
#----------------------- FILM INFORMATION ---------------------#


#----------------------- MAIN FUNCTION ------------------------#
def rental_dataset():
    f = open("../oldJson/rental.json","rb") #abrir ficheiro rentals
    rentals = json.loads(f.read()) #transformar ficheiro para objeto em python
    i = 0 #inicializar contador
    size = len(rentals["rental"])
    while(i < size): #Enquanto houver entradas
        if(rentals["rental"][i]):
            rental = rentals["rental"][i] #Pegar na entrada Rental
            customer_id = rental["customer_id"] #id do cliente
            payment_value = find_payment(str(rental["id"])) #Valor do pagamento
            staff= find_staff(str(rental["staff_id"])) #Informação sobre o staff
            film = find_inventory(str(rental["inventory_id"]))
            try:
                time_rental_date = datetime.strptime(rental["rental_date"], '%Y-%m-%d %H:%M:%S.%f')
            except(ValueError):
                time_rental_date = ""
            try:
                time_return_date = datetime.strptime(rental["return_date"], '%Y-%m-%d %H:%M:%S')
            except(ValueError):
                time_return_date = ""
            rental_date = rental["rental_date"]
            return_date = rental["return_date"]
            if(time_rental_date != "" and time_return_date != ""):
                rental_duration = time_return_date - time_rental_date
            else:
                rental_duration = ""

            rental.pop("staff_id")
            rental.pop("last_update")
            rental.pop("customer_id")
            rental.pop("rental_date")
            rental.pop("return_date")
            rental.pop("inventory_id")

            rental["customer_id"] = customer_id
            rental["rental_date"] = rental_date
            rental["return_date"] = return_date
            rental["rental_duration"] = str(rental_duration)
            rental["payment_value"] = payment_value
            rental["staff"] = staff
            rental["film"] = film
            print("Na iteração nº: " + str(i))
            
        i+=1
    new = open("../newJson/rental.json","w")
    json.dump(rentals,new,indent=3)
#----------------------- MAIN FUNCTION ------------------------#


def main():
    rental_dataset()

main()