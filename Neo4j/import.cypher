-- contry
load csv from "file:///country.csv" as line 
create (co :Country {country : line[1]})

create index on :Country(country)

-- city
load csv from "file:///city.csv" as line
match (co: Country)
where co.country = line[1]
create (ci: City {city: line[0]}), 
       (ci)-[r:pertence_a]->(co)

create index on :City(city)

-- address
using periodic commit 100
load csv from "file:///address.csv" as line
match (ci: City {city: line[3]})-[:pertence_a]->(co: Country {country: line[6]})
create (adr: Address { address: line[0], address2: line[1], district: line[2], code: line[4], phone: line[5]}), 
       (adr)-[r:pertence_a]->(ci)

create index on :Address(address)

-- staff
load csv from "file:///staff.csv" as line
match (adr: Address {address: line[2]})-[:pertence_a]->(ci: City {city : line[3]})
create (st: Staff { first_name: line[0], last_name: line[1], email: line[4], active: line[5], username: line[6], password: line[7]}), 
       (st)-[r:vive_em]->(adr)

-- store
load csv from "file:///store.csv" as line
match (adr: Address {address: line[0]})-[:pertence_a]->(ci: City {city : line[1]})
match (m: Staff {username: line[2]})
create (adr)<-[:localizada_em]-(sto: Store {store_id: line[3]})-[:gerenciado_por]->(m)

create index on :Store(store_id)

load csv from "file:///staff.csv" as line
match (staff: Staff {username: line[6]})
match (store: Store {store_id: line[8]})
create (staff)-[:trabalha_em]->(store)

-- category
load csv from "file:///category.csv" as line
create (:Category{name:line[0]})

create index on :Category(name)

-- actor
load csv from "file:///actor.csv" as line
create (:Actor{first_name: actor_id: line[0], line[1], last_name: line[2]})

create index on :Actor(actor_id)
create index on :Actor(first_name, last_name)

-- customer
load csv from "file:///customer.csv" as line
match (adr: Address {address: line[6]})-[:pertence_a]->(c: City {city: line[7]})
match (st: Store {store_id: line[5]})
create (adr)<-[:vive_em]-(:Customer {first_name: line[0], last_name: line[1], email: line[2], active: line[3], create_date: line[4]})-[:membro_em]->(st)

-- payment
load csv from "file:///payment.csv" as line
match (c: Customer {first_name: line[1], last_name: line[2]})
match (s: Staff {username: line[5]})
create (c)<-[:pago_por]-(p:Payment {amount: toFloat(line[3]), payment_date: line[4], payment_id: line[6]})-[:feito_por]->(s)

create index on :Payment(payment_id)

-- language
load csv from "file:///language.csv" as line
create (:Language {name: line[0]})

create index on :Language(name)

-- film
load csv from "file:///film.csv" as line
match (l:Language {name: line[9]})
create (:Film {title: line[0], description: line[1], release_year: line[2], rental_duration: line[3], rental_rate: line[4], length: line[5], replacement_cost: line[6], rating: line[7], special_features: line[8]})-[:com_lingua]->(l)

create index on :Films(title)

-- film_actor
load csv from "file:///film_actor.csv" as line
match (f: Film {title: line[0]})
match (a: Actor {actor_id: line[1]})
create (f)-[:com_participacao_de]->(a)

match (a:Actor)
remove a.actor_id

-- inventory
load csv from "file:///inventory.csv" as line
match (f: Film {title: line[0]})
match (s: Store {store_id: line[1]})
create (s)-[:tem_filme {numero: line[3]}]->(f)

-- film_category
load csv from "file:///film_category.csv" as line
match (f: Film {title: line[0]})
match (c: Category {name: line[1]})
create (f)-[:com_categoria]->(c)

-- rental
load csv from "file:///rental.csv" as line
match (c: Customer {first_name: line[3], last_name: line[4]})
match (sta: Staff {username: line[5]})
match (f: Film {title: line[6]})
match (sto: Store {store_id: line[7]})
create (sta)<-[:feito_por]-(r:Rental {rental_id: line[0], rental_date: line[1], return_date: line[2]})-[:filme_alugado]->(f),
       (sto)<-[:na_loja]-(r)-[:alugado_por]->(c)

create index on :Rental(rental_id)

-- rental-payment
load csv from "file:///rental-payment.csv" as line
match (p: Payment {payment_id: line[0]})
match (r: Rental {rendtal_id: line[1]})
create (p)-[:alugado]->(r)

match (p:Payment)
remove p.payment_id

match (r:Rental) 
remove r.rental_id
