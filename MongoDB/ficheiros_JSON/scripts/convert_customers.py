import json

#----------------------- ADDRESS INFORMATION ------------------#
def find_address(address_id):
    f = open("../newJson/addresses.json","rb")
    addresses = json.loads(f.read())
    i = 0 #contador para percorrer staff
    address = addresses["address"]
    size = len(address)
    while(i < size):
        if(address[i]["address_id"] == address_id):
            return address[i]
        i+=1
    return 
#----------------------- ADDRESS INFORMATION ------------------#

#----------------------- MAIN FUNCTION ------------------------#
def customers_dataset():
    f = open("../oldJson/customer.json","rb") #abrir ficheiro rentals
    customers = json.loads(f.read()) #transformar ficheiro para objeto em python
    i = 0 #inicializar contador
    size = len(customers["customer"])
    while(i < size): #Enquanto houver entradas
        if(customers["customer"][i]):
            customer = customers["customer"][i]
            name = customer["first_name"] + " " + customer["last_name"]
            mail = customer["email"]
            address = find_address(customer["address_id"])
            address.pop("address_id")
            
            customer.pop("active")
            customer.pop("email")
            customer.pop("create_date")
            customer.pop("last_update")
            customer.pop("store_id")
            customer.pop("address_id")
            customer.pop("first_name")
            customer.pop("last_name")
            
            customer["name"] = name
            customer["email"]= mail
            customer["address"] = address
            
        i += 1
    new = open("../newJson/customers.json","w")
    json.dump(customers,new,indent=3)
#----------------------- MAIN FUNCTION ------------------------#

def main():
    customers_dataset()

main()