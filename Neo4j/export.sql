select staff_id, first_name, last_name, address_id, email, store_id, active, username, password, last_update from staff
into outfile '/var/lib/mysql-files/staff.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from store
into outfile '/var/lib/mysql-files/stores.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from city
into outfile '/var/lib/mysql-files/city.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select address_id, address, address2, district, city_id, postal_code, phone, last_update from address
into outfile '/var/lib/mysql-files/address.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from country
into outfile '/var/lib/mysql-files/country.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from category
into outfile '/var/lib/mysql-files/categories.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from actor
into outfile '/var/lib/mysql-files/actors.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from customer
into outfile '/var/lib/mysql-files/customer.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from payment
into outfile '/var/lib/mysql-files/payment.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from language
into outfile '/var/lib/mysql-files/languages.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select * from film
into outfile '/var/lib/mysql-files/films.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select * from film_actor
into outfile '/var/lib/mysql-files/film_actor.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select * from film_text
into outfile '/var/lib/mysql-files/film_text.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select * from inventory
into outfile '/var/lib/mysql-files/inventory.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select * from film_category
into outfile '/var/lib/mysql-files/film_category.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select * from rental
into outfile '/var/lib/mysql-files/rental.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';


