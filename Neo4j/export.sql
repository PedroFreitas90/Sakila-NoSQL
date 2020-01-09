select * from country
into outfile '/var/lib/mysql-files/country.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select city, country from city
inner join country on city.country_id = country.country_id
into outfile '/var/lib/mysql-files/city.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select address, address2, district, city, postal_code, phone, country from address
inner join city on address.city_id = city.city_id
inner join country on city.country_id = country.country_id
into outfile '/var/lib/mysql-files/address.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select first_name, last_name, address, city, email, active, username, password, store_id from staff
inner join address on address.address_id = staff.address_id
inner join city on city.city_id = address.city_id
into outfile '/var/lib/mysql-files/staff.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select address, city, username, store.store_id from store
inner join address on address.address_id = store.address_id
inner join city on city.city_id = address.city_id
inner join staff on staff.staff_id = store.manager_staff_id
into outfile '/var/lib/mysql-files/store.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select name from category
into outfile '/var/lib/mysql-files/category.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select actor_id, first_name, last_name from actor
into outfile '/var/lib/mysql-files/actor.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select first_name, last_name, email, active, create_date, store_id, address, city from customer
inner join address on address.address_id = customer.address_id
inner join city on address.city_id = city.city_id
into outfile '/var/lib/mysql-files/customer.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select rental_id, customer.first_name, customer.last_name, amount, payment_date, staff.username, payment_id from payment
inner join customer on customer.customer_id = payment.customer_id
inner join staff on staff.staff_id = payment.staff_id
into outfile '/var/lib/mysql-files/payment.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select name from language
into outfile '/var/lib/mysql-files/language.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

select title, description, release_year, rental_duration, rental_rate, film.length, replacement_cost, rating, special_features, language.name from film
inner join language on language.language_id = film.language_id
into outfile '/var/lib/mysql-files/film.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select title, actor.actor_id from film
inner join film_actor on film.film_id = film_actor.film_id
inner join actor on film_actor.actor_id = actor.actor_id
into outfile '/var/lib/mysql-files/film_actor.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select film.title, store_id, film_text.description, count(*) from inventory
inner join film on inventory.film_id = film.film_id
inner join film_text on film_text.film_id = inventory.film_id
group by film.film_id, inventory.store_id
into outfile '/var/lib/mysql-files/inventory.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select title, category.name from film
inner join film_category on film.film_id = film_category.film_id
inner join category on category.category_id = film_category.category_id
into outfile '/var/lib/mysql-files/film_category.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select rental_id, rental_date, return_date, customer.first_name, customer.last_name, staff.username, film.title, inventory.store_id from rental
inner join inventory on inventory.inventory_id = rental.inventory_id
inner join customer on customer.customer_id = rental.customer_id
inner join staff on staff.staff_id = rental.staff_id
inner join film on inventory.film_id = film.film_id
into outfile '/var/lib/mysql-files/rental.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

select payment.payment_id, rental.rental_id from payment
inner join rental on payment.rental_id = rental.rental_id
into outfile '/var/lib/mysql-files/rental-payment.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';


